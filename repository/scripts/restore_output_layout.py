"""Restore unchanged collected artifacts to original outputs paths for source scripts."""
from pathlib import Path
import csv, hashlib, shutil
root=Path(__file__).resolve().parents[1]
with (root/'docs/COPY_MANIFEST.csv').open(encoding='utf-8',newline='') as f:
    for row in csv.DictReader(f):
        if not row['source'].startswith('outputs/'): continue
        source=root/row['destination']; target=root/row['source']
        if target.exists():
            if hashlib.sha256(target.read_bytes()).hexdigest()!=row['sha256']:
                raise RuntimeError(f'Refusing to overwrite differing artifact: {target}')
            continue
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(source,target)
print('Original outputs layout restored from collected artifacts.')
