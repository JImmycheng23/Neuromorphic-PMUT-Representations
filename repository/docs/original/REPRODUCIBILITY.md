# Reproducibility Reference

**Branch:** `v3.0-release`
**Date:** 2026-08-03
**Python:** 3.13.7

## Raw data files

| File | MD5 |
|------|-----|
| `pmut_rx_tx_Air_Glucose_50mM_to_1000mM.xlsx` | `397DC1F0904D471B844DEFABDC9021A7` |
| `low_conc_glucose_sweeps_data_2mM_to_50mM.xlsx` | `A4EDC1E3B1BF8EF71BA4D3A4C09A21AD` |
| `Liquid_Loading_Dataset_Air_DIW_Acetone_IPA.csv` | `F284E4A0F7B1DAB583C7B40CD22F8F98` |

**Data root:** `C:\Users\27010\Desktop\Neumat\Data\PMUT-SNN\`

## Primary benchmark

**Task:** `high-glucose` — 5-class (Glucose 50/100/250/500/1000 mM), 3 sweeps/class, grouped split

The `glucose-ladder` task is **exploratory only**. Low-concentration data (2–20 mM)
have only 1 sweep each — no sweep-level train/test possible.

## Quick regeneration (single command)

```sh
python regenerate_all.py --task high-glucose --window-size 128 --num-seeds 5 --epochs 150
```

Use `--skip-neural`, `--skip-reservoir`, or `--skip-features` to skip compute-heavy stages.

## Step-by-step regeneration commands

All commands run from repo root. Outputs go to `outputs/`.

```sh
# Phase A: Prepare dataset
python prepare_dataset.py --task high-glucose --split grouped --window-size 128

# Phase B: Feature extraction (NB4) — all 15 sweeps
python notebooks/nb4_feature_extraction.py --task high-glucose

# Phase C: Feature ML baselines (NB5)
python notebooks/nb5_feature_ml_baselines.py --task high-glucose

# Phase D: Neural models (5 seeds × 3 folds = 15 runs each)
python train.py --task high-glucose --folds --model cnn1d --num-seeds 5 --epochs 150 --window-size 128
python train.py --task high-glucose --folds --model spiking_cnn1d --num-seeds 5 --epochs 150 --window-size 128
python train.py --task high-glucose --folds --model temporal_lif_snn --num-seeds 5 --epochs 150 --window-size 128
python train.py --task high-glucose --folds --model rate_snn_mlp --num-seeds 5 --epochs 150 --window-size 128

# Phase E: Reservoir models (5 seeds × 3 folds)
python notebooks/nb11_reservoir.py --task high-glucose --folds --num-seeds 5 --window-size 128
python notebooks/nb11_reservoir.py --task high-glucose --folds --num-seeds 5 --lsm --window-size 128

# Phase F: Encoder evaluation (NB9)
python notebooks/nb9_encoder_evaluation.py --task high-glucose --split grouped

# Phase G: Model comparison (NB12)
python notebooks/nb12_model_comparison.py --task high-glucose

# Phase H: Fixed-point (NB13 + NB14)
python notebooks/nb13_fixed_point_lif.py
python notebooks/nb14_fixed_point_pmut.py --task high-glucose --split grouped --window-size 128

# Phase I: HDL (NB15 + NB16)
python notebooks/nb15_hdl_test_vectors.py --task high-glucose --split grouped --window-size 128
python notebooks/nb16_hdl_spec.py --generate-hdl

# Phase J: Central results
python build_central_results.py
python verify_hdl_checklist.py
```

## Key dependencies

```
numpy, scipy, pandas, scikit-learn, matplotlib, openpyxl
torch (for neural models)
```

## Output directory map

```
outputs/
├── datasets/              # Prepared .npz files
├── features/              # NB4: 17 features + 15 diagnostic band plots
├── feature_ml/            # NB5: RF=93.3%, SVM=80.0% + other ML baselines
├── runs/                  # Neural model training (fold-based layout)
│   └── high-glucose_folds_w128/{model}/fold{N}/[seed dirs...]
├── reservoir/             # NB11: ESN + LSM results (fold-based)
│   └── high-glucose/grouped_w128/fold{N}/[lsm/]
├── encoder_evaluation/    # NB9: encoder comparison + plots
├── comparison/            # NB12: cross-model comparison + pipeline selection
├── fixed_point/           # NB13/NB14: bit-width study
├── hdl_test_vectors/      # NB15: test vectors (16-bit, 12-bit)
├── hdl/                   # NB16: HDL spec + Verilog LIF neuron
├── central_results/       # build_central_results.py output (107 rows)
└── REPRODUCIBILITY.md     # This file
```

## Paper comparison notes

The code (this repo) is the reference implementation. Differences from
"Neuromorphic Paper Draft 4.pdf" are documented at the end of README.md.
If the paper reports a number that differs from the central results CSV,
the CSV value is the authoritative result from this codebase.
