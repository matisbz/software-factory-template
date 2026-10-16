#!/usr/bin/env python3
"""Regenerate payload hashes after an intentional template/version edit."""
from pathlib import Path
import hashlib
import json
import sys
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from factory import validate_template
entries = {}
for p in sorted((ROOT / 'template').rglob('*')):
    if p.is_symlink():
        raise SystemExit(f'Symlink not allowed: {p}')
    if p.is_file():
        name = p.relative_to(ROOT / 'template').as_posix()
        policy = 'block' if name == 'AGENTS.md' else 'seed' if name == 'docs/project/CONTEXT.md' else 'managed'
        entries[name] = {'policy': policy, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
manifest = {'schema': 1, 'version': (ROOT / 'VERSION').read_text().strip(), 'files': entries}
(ROOT / 'template-manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n')
validate_template(ROOT)
print(f'Manifest valid: {manifest["version"]}, {len(entries)} payload files')
