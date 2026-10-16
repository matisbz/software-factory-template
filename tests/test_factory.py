"""End-to-end installer regressions. All files are disposable; no inference/network."""
from pathlib import Path
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("factory", ROOT / "scripts/factory.py")
factory = importlib.util.module_from_spec(spec)
spec.loader.exec_module(factory)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="factory-tests-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.source = self.base / "template checkout"
        self.source.mkdir()
        for name in ("template", "scripts", "VERSION", "template-manifest.json"):
            p = ROOT / name
            if p.is_dir():
                shutil.copytree(p, self.source / name)
            else:
                shutil.copy2(p, self.source / name)
        self.target = self.base / "new project with spaces"

    def run_cli(self, command="install", expected=0, *extra):
        result = subprocess.run([sys.executable, str(self.source / "scripts/factory.py"),
                                 command, "--target", str(self.target), *extra],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result

    def write_target(self, name, data):
        p = self.target / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        return p

    def change_upstream(self, name, data, policy=None):
        p = self.source / "template" / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        manifest = json.loads((self.source / "template-manifest.json").read_text())
        old_policy = manifest["files"].get(name, {}).get("policy", "managed")
        manifest["files"][name] = {"sha256": factory.digest(data), "policy": policy or old_policy}
        manifest["version"] = "1.1.0"
        (self.source / "VERSION").write_text("1.1.0\n")
        (self.source / "template-manifest.json").write_text(json.dumps(manifest))

    def snapshot(self):
        return {p.relative_to(self.target).as_posix(): (p.read_bytes(), p.stat().st_mtime_ns)
                for p in self.target.rglob("*") if p.is_file()}

    def test_install_into_new_folder_without_git_or_application_code(self):
        self.run_cli()
        self.assertTrue((self.target / factory.STATE).is_file())
        self.assertEqual(len(list((self.target / ".codex/agents").glob("*.toml"))), 6)
        self.assertFalse((self.target / ".git").exists())
        self.assertFalse((self.target / "src").exists())

    def test_second_install_does_not_rewrite_payload_state_or_backups(self):
        self.run_cli()
        before = self.snapshot()
        self.run_cli()
        self.assertEqual(before, self.snapshot())
        self.assertFalse((self.target / ".software-factory/backups").exists())

    def test_dry_run_and_status_never_create_missing_destination(self):
        self.run_cli("install", 0, "--dry-run")
        self.run_cli("status")
        self.assertFalse(self.target.exists())

    def test_preview_never_mutates_existing_project(self):
        self.run_cli()
        self.change_upstream("docs/software-factory/WORKFLOW.md", b"New workflow\n")
        before = self.snapshot()
        self.run_cli("update", 0, "--dry-run")
        self.run_cli("status")
        self.assertEqual(before, self.snapshot())

    def test_existing_agents_append_preserves_bytes_and_backup(self):
        original = b"# My rules\r\nDo not change the product.\r\n"
        self.write_target("AGENTS.md", original)
        self.run_cli()
        content = (self.target / "AGENTS.md").read_bytes()
        self.assertTrue(content.startswith(original))
        self.assertEqual(content.count(factory.BEGIN), 1)
        backups = list((self.target / ".software-factory/backups").glob("*/AGENTS.md"))
        self.assertEqual([p.read_bytes() for p in backups], [original])
        self.assertEqual(backups[0].stat().st_mode & 0o777, 0o600)
        before = self.snapshot()
        self.run_cli()
        self.assertEqual(before, self.snapshot())

    def test_existing_config_and_role_are_never_overwritten(self):
        cfg = b"# Local custom settings\n[agents]\nenabled = false\n"
        role = b'name = "architect"\ndescription = "Custom"\ndeveloper_instructions = "Custom rules"\n'
        self.write_target(".codex/config.toml", cfg)
        self.write_target(".codex/agents/architect.toml", role)
        self.run_cli(expected=2)
        self.assertEqual((self.target / ".codex/config.toml").read_bytes(), cfg)
        self.assertEqual((self.target / ".codex/agents/architect.toml").read_bytes(), role)
        proposals = list((self.target / ".software-factory/proposals").rglob("*.toml"))
        self.assertEqual(len(proposals), 2)
        before = self.snapshot()
        self.run_cli(expected=2)
        self.assertEqual(before, self.snapshot())

    def test_context_always_preserved_existing_modified_and_deleted(self):
        context = b"# Business context\nPrivate project rules\n"
        p = self.write_target("docs/project/CONTEXT.md", context)
        self.run_cli()
        self.change_upstream("docs/project/CONTEXT.md", b"# Better seed\n")
        self.run_cli("update")
        self.assertEqual(p.read_bytes(), context)
        p.unlink()
        self.run_cli("update")
        self.assertFalse(p.exists())

    def test_unedited_seed_is_not_updated_either(self):
        self.run_cli()
        p = self.target / "docs/project/CONTEXT.md"
        before = p.read_bytes()
        self.change_upstream("docs/project/CONTEXT.md", b"Updated template context\n")
        self.run_cli("update")
        self.assertEqual(p.read_bytes(), before)

    def test_update_intact_file_and_preserve_mode_with_backup(self):
        self.run_cli()
        name = "docs/software-factory/WORKFLOW.md"
        p = self.target / name
        original = p.read_bytes()
        p.chmod(0o600)
        self.change_upstream(name, b"New workflow\n")
        self.run_cli("update")
        self.assertEqual(p.read_bytes(), b"New workflow\n")
        self.assertEqual(p.stat().st_mode & 0o777, 0o600)
        self.assertEqual([p.read_bytes() for p in (self.target / ".software-factory/backups").glob("*/" + name)], [original])
        before = self.snapshot()
        self.run_cli("update")
        self.assertEqual(before, self.snapshot())

    def test_local_customization_without_upstream_change_is_retained(self):
        self.run_cli()
        p = self.write_target("docs/software-factory/WORKFLOW.md", b"Local workflow\n")
        report = self.run_cli("update", 0, "--json")
        action = next(a for a in json.loads(report.stdout)["actions"] if a["path"] == "docs/software-factory/WORKFLOW.md")
        self.assertEqual(action["status"], "customized")
        self.assertEqual(p.read_bytes(), b"Local workflow\n")

    def test_three_way_conflict_preserves_local_and_proposes_upstream(self):
        self.run_cli()
        name = "docs/software-factory/WORKFLOW.md"
        local = b"Personalized local flow\n"
        p = self.write_target(name, local)
        self.change_upstream(name, b"Different upstream flow\n")
        self.run_cli("update", 2)
        self.assertEqual(p.read_bytes(), local)
        proposals = list((self.target / ".software-factory/proposals").glob("*/" + name))
        self.assertEqual([p.read_bytes() for p in proposals], [b"Different upstream flow\n"])
        before = self.snapshot()
        self.run_cli("update", 2)
        self.assertEqual(before, self.snapshot())

    def test_adopting_upstream_resolves_conflict_and_establishes_new_baseline(self):
        self.run_cli()
        name = "docs/software-factory/WORKFLOW.md"
        self.write_target(name, b"Custom\n")
        self.change_upstream(name, b"Upstream 1\n")
        self.run_cli("update", 2)
        self.write_target(name, b"Upstream 1\n")
        self.run_cli("update")
        self.change_upstream(name, b"Upstream 2\n")
        self.run_cli("update")
        self.assertEqual((self.target / name).read_bytes(), b"Upstream 2\n")

    def test_deleted_managed_file_stays_deleted_even_with_upstream_change(self):
        self.run_cli()
        name = "docs/software-factory/WORKFLOW.md"
        p = self.target / name
        p.unlink()
        self.run_cli("update")
        self.change_upstream(name, b"New upstream workflow\n")
        self.run_cli("update", 2)
        self.assertFalse(p.exists())

    def test_update_agents_block_preserves_custom_prefix_and_suffix(self):
        prefix, suffix = b"Custom header\n\n", b"\n\nCustom footer\n"
        self.write_target("AGENTS.md", prefix)
        self.run_cli()
        p = self.target / "AGENTS.md"
        p.write_bytes(p.read_bytes() + suffix)
        incoming = (self.source / "template/AGENTS.md").read_bytes().replace(b"Software Factory:", b"Software Factory v2:")
        self.change_upstream("AGENTS.md", incoming)
        self.run_cli("update")
        self.assertTrue(p.read_bytes().startswith(prefix))
        self.assertTrue(p.read_bytes().endswith(suffix))
        self.assertIn(b"Software Factory v2:", p.read_bytes())

    def test_modified_agents_block_is_preserved(self):
        self.run_cli()
        p = self.target / "AGENTS.md"
        custom = p.read_bytes().replace(b"Software Factory:", b"My factory:")
        p.write_bytes(custom)
        self.run_cli("update")
        incoming = (self.source / "template/AGENTS.md").read_bytes().replace(b"Software Factory:", b"Next factory:")
        self.change_upstream("AGENTS.md", incoming)
        self.run_cli("update", 2)
        self.assertEqual(p.read_bytes(), custom)

    def test_invalid_or_duplicate_agents_markers_fail_before_payload_changes(self):
        for content in (factory.BEGIN, factory.END + factory.BEGIN,
                        factory.BEGIN + factory.END + factory.BEGIN + factory.END):
            with self.subTest(content=content):
                self.write_target("AGENTS.md", content)
                self.run_cli(expected=1)
                self.assertFalse((self.target / ".codex").exists())

    def test_symbolic_link_file_directory_and_state_fail_closed(self):
        outside = self.base / "outside"
        outside.mkdir()
        (outside / "file").write_bytes(b"Do not touch\n")
        for name, target in (("AGENTS.md", outside / "file"), (".codex", outside), (".software-factory", outside)):
            with self.subTest(name=name):
                self.target = self.base / ("symlink case " + name.replace(".", ""))
                self.target.mkdir(exist_ok=True)
                (self.target / name).symlink_to(target)
                self.run_cli(expected=1)
                self.assertEqual((outside / "file").read_bytes(), b"Do not touch\n")
                self.assertEqual(len(list(outside.iterdir())), 1)
                (self.target / name).unlink()

    def test_target_symlink_or_template_subfolder_is_rejected(self):
        outside = self.base / "outside"
        outside.mkdir()
        self.target.symlink_to(outside)
        self.run_cli(expected=1)
        self.target.unlink()
        self.target = self.source / "application"
        self.run_cli(expected=1)
        self.assertFalse(self.target.exists())

    def test_manifest_traversal_and_corruption_do_not_write_target(self):
        mpath = self.source / "template-manifest.json"
        original = mpath.read_bytes()
        for bad in (b"not json", json.dumps({"schema": 1, "version": "1.0.0", "files": {"../escape": {"policy": "managed", "sha256": "0" * 64}}}).encode()):
            mpath.write_bytes(bad)
            self.run_cli(expected=1)
            self.assertFalse(self.target.exists())
        mpath.write_bytes(original)
        (self.source / "template/AGENTS.md").write_bytes(b"Tampered\n")
        self.run_cli(expected=1)
        self.assertFalse(self.target.exists())

    def test_invalid_toml_or_unavailable_model_in_base_payload_is_rejected(self):
        self.change_upstream(".codex/agents/architect.toml", b"name = [ broken\n")
        self.run_cli(expected=1)
        self.assertFalse(self.target.exists())
        self.change_upstream(".codex/agents/architect.toml", b'name = "architect"\ndescription = "Role"\ndeveloper_instructions = "Work"\nmodel = "unavailable-model"\n')
        self.run_cli(expected=1)
        self.assertFalse(self.target.exists())

    def test_source_symlink_is_rejected(self):
        p = self.source / "template/docs/software-factory/WORKFLOW.md"
        p.unlink()
        p.symlink_to(ROOT / "README.md")
        self.run_cli(expected=1)
        self.assertFalse(self.target.exists())

    def test_corrupt_installed_state_does_not_mutate_payload(self):
        self.run_cli()
        (self.target / factory.STATE).write_text('{"schema": 1, "files": {"../escape": {"policy": "managed"}}}')
        before = self.snapshot()
        self.run_cli("update", 1)
        self.assertEqual(before, self.snapshot())

    def test_destination_type_collision_is_detected_before_any_payload_write(self):
        self.write_target("docs", b"Not a directory\n")
        self.run_cli(expected=1)
        self.assertFalse((self.target / "AGENTS.md").exists())
        self.assertFalse((self.target / ".codex").exists())

    def test_lock_prevents_concurrent_installers(self):
        self.run_cli()
        lock = self.target / ".software-factory/.install.lock"
        lock.mkdir()
        (lock / "owner").write_text("pid=test\n")
        before = self.snapshot()
        self.run_cli("update", 1)
        self.assertEqual(before, self.snapshot())

    def test_altered_proposal_fails_without_overwriting_it(self):
        self.write_target(".codex/config.toml", b"# Custom config\n")
        self.run_cli(expected=2)
        p = next((self.target / ".software-factory/proposals").glob("*/.codex/config.toml"))
        p.write_bytes(b"Personal notes in proposal\n")
        before = self.snapshot()
        self.run_cli(expected=1)
        self.assertEqual(before, self.snapshot())

    def test_upstream_retired_file_is_never_deleted(self):
        self.run_cli()
        name = "docs/software-factory/WORKFLOW.md"
        original = (self.target / name).read_bytes()
        (self.source / "template" / name).unlink()
        mpath = self.source / "template-manifest.json"
        manifest = json.loads(mpath.read_text())
        del manifest["files"][name]
        mpath.write_text(json.dumps(manifest))
        self.run_cli("update")
        self.assertEqual((self.target / name).read_bytes(), original)
        state = json.loads((self.target / factory.STATE).read_text())
        self.assertTrue(state["files"][name]["retired"])

    def test_future_version_adds_new_file_without_affecting_application(self):
        self.run_cli()
        code = self.write_target("src/application.py", b"# Existing application\n")
        self.change_upstream("docs/software-factory/NEW.md", b"New guide\n")
        self.run_cli("update")
        self.assertEqual((self.target / "docs/software-factory/NEW.md").read_bytes(), b"New guide\n")
        self.assertEqual(code.read_bytes(), b"# Existing application\n")

    def test_policy_changes_fail_before_modifying_context(self):
        self.run_cli()
        self.change_upstream("docs/project/CONTEXT.md", b"New context\n", policy="managed")
        before = self.snapshot()
        self.run_cli("update", 1)
        self.assertEqual(before, self.snapshot())

    def test_update_requires_registered_installation(self):
        self.run_cli("update", 1)
        self.assertFalse(self.target.exists())

    def test_atomic_write_detects_file_changed_since_preview(self):
        self.write_target("AGENTS.md", b"New edit\n")
        with self.assertRaises(factory.FactoryError):
            factory.write_atomic(self.target, "AGENTS.md", b"Replacement\n", b"Old edit\n")
        self.assertEqual((self.target / "AGENTS.md").read_bytes(), b"New edit\n")

    def test_interrupted_partial_install_can_be_retried(self):
        manifest = factory.validate_template(self.source)
        original_replace = os.replace
        calls = 0
        def fail_once(src, dst):
            nonlocal calls
            calls += 1
            if calls == 3:
                raise OSError("simulated disk failure")
            return original_replace(src, dst)
        with patch.object(factory.os, "replace", side_effect=fail_once):
            with self.assertRaises(OSError):
                factory.apply(self.source, self.target, manifest)
        self.assertFalse((self.target / ".software-factory/.install.lock").exists())
        self.run_cli()
        self.run_cli("status")
        self.assertEqual(len(list((self.target / ".codex/agents").glob("*.toml"))), 6)


if __name__ == "__main__":
    unittest.main()
