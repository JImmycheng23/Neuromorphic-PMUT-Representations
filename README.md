# Neuromorphic PMUT representations — code, data and supporting outputs


This pull-request package contains the author-designated final Git-paper code/results under `repository/`, with recovered raw data, regenerated model exports and supporting validation. The nested layout preserves the checked reproduction commands and provenance paths.

| Start here | Location |
|---|---|
| Git-paper source, archived results, figures and hardware prototype | [repository/](repository/) |
| Raw measurements | [repository/data/raw/](repository/data/raw/) |
| Regenerated datasets, fitted models and precision evidence | [generated/](generated/) |
| Reproduction commands | `reproduce_supplement.py` (run from this directory) |
| Integration status and remaining requirements | [INTEGRATION_STATUS.md](INTEGRATION_STATUS.md) |

Prepared 18 October 2026 from the author-designated final `Git-paper` package, raw files recovered from `Neumat/Data/PMUT-SNN`, and source in `Neumat/Data/pmut_snn_models`. All 286 source-backed files in the final extraction match that source by SHA-256. All three raw files match the historical MD5 values in its reproducibility document. Original folders were not modified.

Staged CLI help corrections are recorded in `CODE_AMENDMENTS.json`. They fix two help-formatting failures and describe the actual non-overlapping default; model calculations and archived results are unchanged. The current [requirements coverage audit](REQUIREMENTS_AUDIT.md) identifies covered and remaining partial requirements.

**Reporting scope:** SpikingCNN1D covers fold 0 only (five seeds) and remains incomplete. Extra saved folds are archival material and are excluded from reported performance. HDL is a single-neuron prototype, not a verified full-reservoir implementation. See [study scope](STUDY_SCOPE.md) and the [precision protocol](generated/precision_regeneration/README.md).

## What is included

| Material | Location | Check performed |
|---|---|---|
| Three original raw acquisition files | `repository/data/raw/` | SHA-256 copy checks and agreement with recorded MD5 hashes |
| Main five-concentration data: 15 sweeps, 90,000 samples | `generated/data/high_glucose_90000_samples.csv` | 6,000 ordered points per sweep; original workbook row identifiers retained |
| Sweep and window provenance | `generated/data/sweep_inventory.csv`, `window_provenance.csv`, `window_fold_assignments.csv` | 690 windows; frequency boundaries; original Excel rows; 2,070 fold/partition assignments |
| Three correct rotation datasets | `generated/datasets/fold0.npz` through `fold2.npz` | Each has 230/230/230 windows and disjoint train/validation/test parent sweeps; recorded normalisation matches exactly |
| Regenerated features | `generated/features/high_glucose_features_regenerated.csv` | All 17 selected feature columns reproduce the archived table within numerical tolerance, including missing-value locations |
| Original checkpoints: 15 CNN + 15 SpikingCNN archived files | `repository/models/high-glucose_folds_w128/` | Inference checked for all 30 files; only five fold-0 SpikingCNN checkpoints are in the reported study |
| Fitted feature classifiers: 18 legacy + 18 corrected-imputation models | `generated/models/features/` | Legacy scores match archive; every saved pipeline was reloaded and checked |
| Fitted reservoir exports: 15 ESN + 15 membrane LSM + 3 spike LSM | `generated/models/reservoir/` | All 33 reproduce stored predictions and probabilities; every export was reloaded and checked |
| Precision-specific fitted exports and traces | `generated/precision_regeneration/` | All five accuracy values reproduced with explicit grouped-split metadata; see historical-identity qualification below |
| Per-run class probabilities and predictions | `generated/neural_checkpoint_validation/`, reservoir NPZ exports, precision CSVs | Newly recorded inference traces with targets and parent sweep keys |
| Source, existing figures, archived results, single-neuron RTL and test vectors | `repository/` | Preserved source-backed files; presence of RTL/test vectors is not hardware verification |
| Supplementary Table S1: imputation sensitivity | `generated/tables/S1_feature_imputation_comparison.csv` | Isolates full-table versus training-fold-only median fitting |
| Supplementary Table S2: all 104 model artifacts | `generated/tables/S2_model_exports.csv` | Distinguishes original checkpoints from regenerated fitted models |

The two supplementary low-concentration/baseline files are supplied as original acquisition evidence. They are not additional independent measurements for the five-class benchmark. The primary high-glucose workbook is `pmut_rx_tx_Air_Glucose_50mM_to_1000mM.xlsx`, sheet `AllSamples`.

## Supplementary Table S1 — effect of fitting imputation inside each training fold

| Classifier | Archived accuracy (%) | Training-fold-only accuracy (%) | Archived macro-F1 (%) | Training-fold-only macro-F1 (%) |
|---|---:|---:|---:|---:|
| SVM (RBF) | 66.7 | 73.3 | 63.1 | 66.5 |
| SVM (Linear) | 80.0 | 73.3 | 78.1 | 72.6 |
| Random Forest | 93.3 | 93.3 | 93.1 | 93.1 |
| KNN (k=3) | 66.7 | 66.7 | 64.4 | 64.4 |
| KNN (k=5) | 60.0 | 60.0 | 46.7 | 46.7 |
| MLP | 86.7 | 86.7 | 86.7 | 86.3 |

The Random Forest accuracy (93.3%) and macro-F1 (93.1%) are retained with training-fold-only imputation. RBF and linear SVM scores change; MLP macro-F1 also changes. The main manuscript keeps the archived comparison explicitly labelled and reports this new sensitivity check separately. No original result files were overwritten.

## Reproduce the supplement

Use an environment containing the dependencies in `repository/requirements.txt`; the exact environment used here is in `generated/ENVIRONMENT.json`. The existing source virtual environment was used for this verification. A new clean installation was not tested. Run from this directory:

```powershell
python reproduce_supplement.py --stage data
python reproduce_supplement.py --stage features
python reproduce_supplement.py --stage reservoir
python reproduce_supplement.py --stage neural
python reproduce_supplement.py --stage precision
python reproduce_supplement.py --stage reload
```

These commands use package-relative raw-data paths and write only into `generated/`. The copied original entry points retain their historical defaults; they are preserved for provenance. The wrapper explicitly supplies `repository/data/raw` and avoids reliance on the original absolute Windows data path.

To load a reservoir export independently:

```powershell
python infer_exported_reservoir.py generated/models/reservoir/ESN/fold0_seed7 --dataset generated/datasets/fold0.npz --already-normalized
```

The NPZ exports contain input/recurrent weights, biases, Ridge coefficients/intercepts/classes, training normalisation and class labels. Their adjacent JSON files specify dynamics, warm-up, state reduction, fold, seed and validation results. Feature-model bundles contain the fitted sklearn pipeline, predictor order, labels and (for legacy runs) the external full-table medians. They can be loaded with joblib in the recorded environment.

## Interpretation and remaining limits

- Regenerated fitted models are new exports from the recovered raw data and original source. They are not presented as historical model files recovered from disk. Reservoir probabilities match historical arrays to numerical tolerance, and legacy feature scores match historical summaries.
- The precision regeneration uses the source-defined grouped split, seed 42, membrane-state reduction and a refitted floating-point Ridge at each precision. It reproduces 83.9%, 84.8%, 83.9%, 75.2% and 71.7%. Original per-window precision predictions were absent, so equal aggregate accuracy does not establish identity with every historical prediction. New complete predictions and partition metadata are supplied.
- The archived processed grouped NPZ has 368/92/230 training/validation/test windows, with shared training/validation parent sweeps. It is kept as an archived artifact. The new `generated/datasets/fold*.npz` files implement the separately recorded 230/230/230 sweep-disjoint rotation and must be used for that benchmark.
- The archived spike-LSM fitted exports included here cover one seed per fold. The latest manuscript's selected five-seed majority-vote analysis was checked separately; this historical export index must not be used as its aggregate table. No decay-sensitivity experiment is claimed.
- Phase/IQ checks strongly support degrees for the raw high-glucose phase field: see `generated/data/phase_units_audit.csv`. The loaders preserve this channel for model reproduction; no phase correction or unwrapping was silently applied.
- The RTL remains a single-neuron module. Ten-neuron software traces are not proof of simulation or a complete 300-neuron FPGA classifier. No HDL simulator evidence or hardware measurements were generated.
- Licensing, final author metadata and acquisition conditions such as the 10 V convention still require author confirmation. The citation metadata are a draft; this package does not assert publication acceptance.

## Provenance files

- `raw_data_inventory.json`: original locations, sizes, SHA-256 and MD5 values.
- `source_reconciliation.csv`: checks against the designated final extraction and original source.
- `final_results_audit.json` and `final_results_per_run.csv`: historical probability-averaged result reconciliation from the earlier draft. They are not the latest manuscript's selected majority-vote aggregates.
- `generated/*validation.json`: assertions and results for each regeneration or inference check.
- `MANIFEST.csv`: checksum and size of every packaged file except the manifest itself; caches are excluded.
- The old extraction status in `repository/docs/STATUS.md` is retained as a historical record. This index supersedes its statements that raw data and fitted exports are unavailable.
