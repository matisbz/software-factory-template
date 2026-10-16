#!/usr/bin/env python3
"""Local, dependency-free installer. Requires Python 3.11+. No network or Git writes."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile
import uuid

try:
    import tomllib
except ImportError:
    raise SystemExit("Software Factory requiere Python 3.11 o superior; usa el runtime disponible en Codex.")

ROOT = Path(__file__).resolve().parent.parent
STATE = ".software-factory/manifest.json"
BEGIN = b"<!-- software-factory:begin -->"
END = b"<!-- software-factory:end -->"
ROLES = {"architect", "solution_designer", "uxui_designer", "developer", "qa_engineer", "pr_reviewer"}


class FactoryError(Exception):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def relative(value: str) -> str:
    p = PurePosixPath(value)
    if (not value or p.is_absolute() or p.as_posix() != value
            or ".." in p.parts or ".git" in p.parts or "\\" in value):
        raise FactoryError(f"Ruta no permitida: {value!r}")
    return value


def safe_path(root: Path, name: str) -> Path:
    path = root / relative(name)
    current = root
    for part in PurePosixPath(name).parts:
        current = current / part
        if current.is_symlink():
            raise FactoryError(f"Enlace simbólico no permitido: {current}")
        if current.exists() and current != path and not current.is_dir():
            raise FactoryError(f"El padre no es un directorio: {current}")
    if path.exists() and not path.is_file():
        raise FactoryError(f"Se esperaba un archivo: {path}")
    return path


def read(root: Path, name: str) -> bytes | None:
    p = safe_path(root, name)
    return p.read_bytes() if p.exists() else None


def parse_json(data: bytes, label: str) -> dict:
    try:
        obj = json.loads(data)
        if not isinstance(obj, dict):
            raise ValueError("se esperaba un objeto")
        return obj
    except (ValueError, UnicodeError) as exc:
        raise FactoryError(f"JSON inválido en {label}: {exc}") from exc


def block(data: bytes) -> tuple[int, int] | None:
    if BEGIN not in data and END not in data:
        return None
    if data.count(BEGIN) != 1 or data.count(END) != 1:
        raise FactoryError("Marcadores duplicados o incompletos en AGENTS.md")
    start, end = data.index(BEGIN), data.index(END) + len(END)
    if data.index(END) < start:
        raise FactoryError("Marcadores desordenados en AGENTS.md")
    return start, end


def validate_template(source: Path) -> dict:
    raw = read(source, "template-manifest.json")
    if raw is None:
        raise FactoryError("Falta template-manifest.json")
    manifest = parse_json(raw, "template-manifest.json")
    if manifest.get("schema") != 1 or not isinstance(manifest.get("files"), dict):
        raise FactoryError("Manifiesto de plantilla incompatible")
    version = read(source, "VERSION")
    if version is None or not re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")):
        raise FactoryError("Versión inválida")
    if version.decode().strip() != manifest["version"]:
        raise FactoryError("VERSION no coincide con el manifiesto")
    listed = set(manifest["files"])
    paths = list((source / "template").rglob("*"))
    if any(p.is_symlink() for p in paths):
        raise FactoryError("La plantilla contiene un enlace simbólico")
    actual = {p.relative_to(source / "template").as_posix()
              for p in paths if not p.is_dir()}
    if actual != listed:
        raise FactoryError("Los archivos de template/ no coinciden con el manifiesto")
    for name, entry in manifest["files"].items():
        relative(name)
        if name.startswith(".software-factory/") and name != ".software-factory/.gitignore":
            raise FactoryError("La plantilla intenta escribir en el estado reservado")
        if not isinstance(entry, dict) or entry.get("policy") not in {"managed", "seed", "block"}:
            raise FactoryError(f"Política inválida: {name}")
        if entry["policy"] == "block" and name != "AGENTS.md":
            raise FactoryError("La política block solo admite AGENTS.md")
        if name == "docs/project/CONTEXT.md" and entry["policy"] != "seed":
            raise FactoryError("El contexto debe conservar la política seed")
        data = read(source / "template", name)
        if data is None or digest(data) != entry.get("sha256"):
            raise FactoryError(f"Integridad incorrecta: {name}")
        if name.endswith(".toml"):
            try:
                tomllib.loads(data.decode())
            except (ValueError, UnicodeError) as exc:
                raise FactoryError(f"TOML inválido: {name}: {exc}") from exc
    cfg = tomllib.loads(read(source / "template", ".codex/config.toml").decode())
    if cfg != {"agents": {"enabled": True, "max_concurrent_threads_per_session": 3}}:
        raise FactoryError("Configuración base inesperada; revisar validador y documentación")
    names = set()
    for name in listed:
        if name.startswith(".codex/agents/"):
            cfg = tomllib.loads(read(source / "template", name).decode())
            if set(cfg) != {"name", "description", "developer_instructions"}:
                raise FactoryError(f"Campos de subagente inesperados: {name}")
            if any(not isinstance(v, str) or not v.strip() for v in cfg.values()):
                raise FactoryError(f"Subagente incompleto: {name}")
            if cfg["name"] in names:
                raise FactoryError("Nombre de subagente duplicado")
            names.add(cfg["name"])
    if names != ROLES:
        raise FactoryError("Deben existir exactamente los seis roles del núcleo")
    factory_block = read(source / "template", "AGENTS.md")
    span = block(factory_block)
    if span != (0, len(factory_block.rstrip(b"\n"))):
        raise FactoryError("AGENTS.md debe contener solo el bloque gestionado")
    return manifest


def load_state(target: Path) -> dict:
    data = read(target, STATE)
    if data is None:
        return {"schema": 1, "files": {}}
    obj = parse_json(data, STATE)
    if obj.get("schema") != 1 or not isinstance(obj.get("files"), dict):
        raise FactoryError("Estado incompatible; no se ha escrito ningún archivo")
    for name, entry in obj["files"].items():
        relative(name)
        if not isinstance(entry, dict) or entry.get("policy") not in {"managed", "seed", "block"}:
            raise FactoryError(f"Estado inválido: {name}")
        baseline = entry.get("baseline")
        if baseline is not None and not re.fullmatch(r"[a-f0-9]{64}", baseline):
            raise FactoryError(f"Huella de estado inválida: {name}")
    return obj


def plan(source: Path, target: Path, manifest: dict, state: dict) -> tuple[list, dict]:
    actions, entries = [], dict(state["files"])
    for name, meta in sorted(manifest["files"].items()):
        incoming = read(source / "template", name)
        current = read(target, name)
        old = state["files"].get(name)
        policy = meta["policy"]
        if old and old["policy"] != policy:
            raise FactoryError(f"Cambio de política requiere revisión: {name}")
        baseline = old.get("baseline") if old else None
        status, result, owned = "keep", current, baseline
        if policy == "seed":
            if current is None and old is None:
                status, result = "create", incoming
        elif policy == "block":
            span = block(current) if current is not None else None
            new_span = block(incoming)
            new_block = incoming[new_span[0]:new_span[1]]
            if current is None:
                if old is None:
                    status, result, owned = "create", incoming, digest(new_block)
                elif baseline == digest(new_block):
                    status = "deleted"
                else:
                    status = "conflict"
            elif span is None:
                if old is None:
                    separator = b"" if current.endswith(b"\n\n") else b"\n\n"
                    status, result, owned = "append", current + separator + incoming, digest(new_block)
                elif baseline == digest(new_block):
                    status = "customized"
                else:
                    status = "conflict"
            else:
                local_block = current[span[0]:span[1]]
                if local_block == new_block:
                    owned = digest(new_block)
                elif baseline == digest(local_block):
                    status, result, owned = "update", current[:span[0]] + new_block + current[span[1]:], digest(new_block)
                elif baseline == digest(new_block):
                    status = "customized"
                else:
                    status = "conflict"
        elif current == incoming:
            owned = digest(incoming)
        elif current is None and old is None:
            status, result, owned = "create", incoming, digest(incoming)
        elif current is not None and baseline == digest(current):
            status, result, owned = "update", incoming, digest(incoming)
        elif baseline == digest(incoming):
            status = "deleted" if current is None else "customized"
        else:
            status = "conflict"
        proposal = f".software-factory/proposals/{digest(incoming)}/{name}"
        if status == "conflict":
            existing = read(target, proposal)
            if existing is not None and existing != incoming:
                raise FactoryError(f"Propuesta alterada; conservar y mover antes de reintentar: {proposal}")
        actions.append({"path": name, "status": status, "before": current,
                        "after": result, "proposal": proposal, "incoming": incoming})
        entries[name] = {"policy": policy, "baseline": owned,
                         "offered_sha256": meta["sha256"], "pending": status == "conflict"}
    for name in set(state["files"]) - set(manifest["files"]):
        read(target, name)  # Validate the old path; retired files are always retained.
        entries[name] = {**entries[name], "retired": True}
        actions.append({"path": name, "status": "retained"})
    next_state = {"schema": 1, "template_version": manifest["version"], "files": entries}
    return actions, next_state


def write_atomic(root: Path, name: str, data: bytes, expected: bytes | None) -> None:
    p = safe_path(root, name)
    if read(root, name) != expected:
        raise FactoryError(f"Archivo cambiado durante la instalación: {name}")
    private = name.startswith((".software-factory/backups/", ".software-factory/proposals/"))
    mode = stat.S_IMODE(p.stat().st_mode) if p.exists() else 0o600 if private else 0o644
    current = root
    for part in p.parent.relative_to(root).parts:
        current = current / part
        current.mkdir(mode=0o700 if private else 0o755, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=".factory-", dir=p.parent)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.chmod(temp, mode)
        if read(root, name) != expected:
            raise FactoryError(f"Archivo cambiado durante la escritura: {name}")
        safe_path(root, name)
        os.replace(temp, p)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def apply(source: Path, target: Path, manifest: dict) -> tuple[list, dict]:
    # Exclusive installer lock, never auto-break a lock belonging to another process.
    safe_path(target, ".software-factory/.install.lock/owner")
    target.mkdir(parents=True, exist_ok=True)
    internal = target / ".software-factory"
    internal.mkdir(mode=0o700, exist_ok=True)
    lock = internal / ".install.lock"
    try:
        lock.mkdir(mode=0o700)
    except FileExistsError as exc:
        raise FactoryError("Otra instalación o bloqueo pendiente: .software-factory/.install.lock") from exc
    try:
        (lock / "owner").write_text(f"pid={os.getpid()}\n")
        before_state = read(target, STATE)
        state = load_state(target)
        actions, next_state = plan(source, target, manifest, state)
        tx = uuid.uuid4().hex
        # Preflight every backup path before touching a payload file.
        for action in actions:
            if action["status"] in {"update", "append"}:
                read(target, f".software-factory/backups/{tx}/{action['path']}")
        read(target, f".software-factory/backups/{tx}/{STATE}")
        for action in actions:
            status, name = action["status"], action["path"]
            if status == "conflict":
                p = action["proposal"]
                if read(target, p) is None:
                    write_atomic(target, p, action["incoming"], None)
            elif status in {"create", "update", "append"}:
                if action["before"] is not None:
                    backup = f".software-factory/backups/{tx}/{name}"
                    write_atomic(target, backup, action["before"], None)
                write_atomic(target, name, action["after"], action["before"])
        encoded = (json.dumps(next_state, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()
        if before_state != encoded:
            if before_state is not None:
                write_atomic(target, f".software-factory/backups/{tx}/{STATE}", before_state, None)
            write_atomic(target, STATE, encoded, before_state)
        return actions, next_state
    finally:
        (lock / "owner").unlink(missing_ok=True)
        lock.rmdir()


def target_root(value: str, source: Path) -> Path:
    raw = Path(value).expanduser().absolute()
    if raw.is_symlink():
        raise FactoryError("El destino no puede ser un enlace simbólico")
    target = raw.resolve()
    if target.exists() and not target.is_dir():
        raise FactoryError("El destino debe ser un directorio")
    if target == Path(target.anchor) or target == Path.home().resolve():
        raise FactoryError("Indica una carpeta de proyecto, no la raíz ni tu carpeta personal")
    if target == source or source.is_relative_to(target) or target.is_relative_to(source):
        raise FactoryError("Usa un proyecto separado de la plantilla")
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["validate", "install", "update", "status"])
    parser.add_argument("--target", help="Carpeta del proyecto; puede no existir")
    parser.add_argument("--source", default=str(ROOT), help="Checkout local de la plantilla")
    parser.add_argument("--dry-run", action="store_true", help="Plan sin escribir archivos")
    parser.add_argument("--json", action="store_true", help="Informe legible por máquinas")
    args = parser.parse_args(argv)
    try:
        source = Path(args.source).resolve()
        manifest = validate_template(source)
        if args.command == "validate":
            print(f"Plantilla {manifest['version']}: TOML, seis roles e integridad correctos.")
            return 0
        if not args.target:
            parser.error("--target es obligatorio")
        target = target_root(args.target, source)
        state = load_state(target)
        if args.command == "update" and read(target, STATE) is None:
            raise FactoryError("Proyecto sin instalación registrada; usa install")
        if args.command in {"status"} or args.dry_run:
            actions, next_state = plan(source, target, manifest, state)
        else:
            actions, next_state = apply(source, target, manifest)
        report = {"version": manifest["version"], "target": str(target),
                  "dry_run": args.dry_run or args.command == "status",
                  "actions": [{k: a[k] for k in ("path", "status", "proposal") if k in a and (k != "proposal" or a["status"] == "conflict")} for a in actions]}
        conflicts = sum(a["status"] == "conflict" for a in actions)
        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(f"Software Factory {manifest['version']} → {target}")
            for a in report["actions"]:
                print(f"{a['status']:>8}  {a['path']}")
                if a["status"] == "conflict":
                    print(f"          propuesta: {a['proposal']}")
            if conflicts:
                print(f"{conflicts} personalizaciones o borrados preservados. Revisa propuestas; salida 2.")
            print("Abre una conversación nueva en el proyecto de Codex para cargar los agentes.")
        return 2 if conflicts else 0
    except (FactoryError, OSError, ValueError, TypeError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        print("No se fuerza ningún reemplazo. Si hubo escrituras previas al fallo, revisa .software-factory/backups/ y vuelve a ejecutar.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
