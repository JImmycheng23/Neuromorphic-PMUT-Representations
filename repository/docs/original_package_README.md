# PMUT representations paper — local GitHub review package

Prepared 18 October 2026 from the requested pmut_snn_models folder, using the attached repository-preparation email as the requirements reference. Intended repository: https://github.com/mz503/Neuromorphic-PMUT-Representations

**Author review required. This package has not been pushed or certified reproducible.**

Start with [requirements coverage](docs/REQUIREMENTS_CHECKLIST.csv), [missing evidence and discrepancies](docs/STATUS.md), [copied-file provenance](docs/COPY_MANIFEST.csv), and [model inventory](models/MODEL_INDEX.csv).

## Contents

- data/raw/, data/metadata/, data/processed/, data/splits/: raw-data placeholders, derived metadata, existing arrays/features and saved-run split assignments.
- src/, notebooks/, scripts/ and original root .py entry points: unchanged source plus one explicitly generated output-layout helper.
- configs/: settings extracted from saved JSON and literal feature definitions; not complete standalone experiment configs.
- models/: 30 saved CNN/SpikingCNN state dictionaries, grouped by model/fold/seed.
- results/: predictions, metrics, histories, summaries and exploratory SpikingCNN evidence.
- figures/: existing generated image exports; final manuscript numbering needs reconciliation.
- hardware/: single-neuron Verilog, specification and existing test vectors.
- docs/: original documentation, extraction manifest, exclusions, status and workflow guidance.

All 286 copied source-backed files were hash-verified. Other clearly identified files were generated to help review the extraction. Original copied code/data/results were not changed. Virtual environments, Git history, caches, assistant settings and outputs for out-of-scope neural/encoder/random-window experiments were excluded. Shared library code and original central comparison tables may still describe those architectures; retained tables are provenance, not manuscript-approved results.

Installation and reproduction: see [workflow guidance](docs/REPRODUCTION.md). requirements.txt pins the current source virtual environment; it does not prove the training-time environment. Raw data and complete fitted-model exports are missing. No license was invented.
