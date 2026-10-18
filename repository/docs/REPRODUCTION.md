# Reproduction entry points and tested scope

The current assembled supplement includes raw data and generated exports. From the supplement root (one directory above this repository), use the staged reproduction wrapper:

```powershell
python reproduce_supplement.py --stage data
python reproduce_supplement.py --stage features
python reproduce_supplement.py --stage reservoir
python reproduce_supplement.py --stage neural
python reproduce_supplement.py --stage precision
python reproduce_supplement.py --stage reload
```

The wrapper supplies package-relative raw paths. Data, fitted feature/reservoir exports, original neural checkpoint inference, precision scores and export reloading have supporting validation records under generated/. This is not a claim that every original training/notebook workflow was executed top-to-bottom in a fresh environment.

From this repository root, the original dataset CLI can be run explicitly as:

```powershell
python prepare_dataset.py --task high-glucose --split grouped --window-size 128 --stride 128 --data-root data/raw
```

Its grouped NPZ is separate from the sweep-disjoint three-fold rotation. Use ../generated/datasets/fold0.npz through fold2.npz for the latter.

The source default stride is one full window (non-overlapping), including when --stride is omitted. Two CLI help-only corrections are recorded in ../CODE_AMENDMENTS.json. Original notebook scripts still retain historical paths; use the wrapper or explicitly review those paths. Current dependency versions are in ../generated/ENVIRONMENT.json. A fresh clean installation and every original script's full training workflow have not been certified.

Reporting scope remains SpikingCNN fold 0 only and a single-neuron HDL prototype. See ../STUDY_SCOPE.md, ../generated/precision_regeneration/README.md and ../REQUIREMENTS_AUDIT.md. Original extraction instructions are preserved in docs/original/ for provenance.
