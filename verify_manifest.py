from __future__ import annotations

import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'MANIFEST_SHA256.json').read_text())
failed = []
for rel, expected in manifest.items():
    path = root / rel
    if not path.exists():
        failed.append({'file': rel, 'reason': 'missing'})
        continue
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        failed.append({'file': rel, 'expected': expected, 'actual': actual})
if failed:
    raise SystemExit(json.dumps(failed, indent=2))
print(f'Verified {len(manifest)}/{len(manifest)} files')
