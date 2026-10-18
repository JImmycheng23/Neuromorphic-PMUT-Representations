# PMUT Neuromorphic Classification

Piezoelectric Micromachined Ultrasonic Transducer (PMUT) fluid classification using
spiking neural networks, reservoir computing (ESN/LSM), and CNNs. Impedance sweeps are
recorded across a frequency ramp (100 kHz – 2.5 MHz) with four channels per sweep:
**amplitude**, **phase**, **x_v** (in-phase), **y_v** (quadrature).

**Primary benchmark:** 5-class high-glucose (50/100/250/500/1000 mM), 3 physical sweeps
per class, 3-fold sweep-level rotation with 5 seeds.

**GitHub:** [JImmycheng23/PMUT_SNN](https://github.com/JImmycheng23/PMUT_SNN)

---

## Latest Results (2026-08-03 — full regeneration)

All results below are from a single frozen commit, fully reproducible via `regenerate_all.py`.
Window-level results use 3-fold sweep rotation × 5 seeds (15 runs per model).
Feature ML results use 3-fold stratified cross-validation over 15 sweep feature vectors.

### Window-Level (Neural + Reservoir)

### Window-Level (Neural + Reservoir)

| Model | Type | Fold 0 | Fold 1 | Fold 2 | **Mean ± Std** |
|-------|------|--------|--------|--------|----------------|
| SpikingCNN1D | Learned spiking | 79.6% | 73.6% | 83.5% | **78.9% ± 5.0%** |
| CNN1D | Convolutional | 72.4% | 69.2% | 88.7% | **76.8% ± 10.4%** |
| TemporalLIFSNN | Learned spiking | 77.0% | 66.8% | 74.4% | **72.8% ± 5.3%** |
| RateSNNMLP | Learned spiking | 73.8% | 67.8% | 71.2% | **71.0% ± 3.0%** |
| ESN (tanh) | Rate-coded reservoir | 70.1% | 85.7% | 86.1% | **80.6% ± 9.1%** |
| LSM (spike readout) | Spiking reservoir | 70.9% | 87.8% | 89.1% | **82.6% ± 9.1%** |
| LSM (membrane readout) | Spiking reservoir | 67.9% | 81.7% | 84.7% | **78.1% ± 9.0%** |

### Sweep-Level (Reservoir — mean_logits aggregation)

| Model | Fold 0 | Fold 1 | Fold 2 | **Mean** |
|-------|--------|--------|--------|----------|
| ESN (tanh) | 80.0% | 80.0% | 100.0% | **86.7%** |
| LSM (membrane) | 60.0% | 80.0% | 100.0% | **80.0%** |
| LSM (spikes) | 100.0% | 100.0% | 100.0% | **100.0%** |

### Sweep-Level (Feature ML)

| Model | Accuracy | Macro F1 |
|-------|----------|----------|
| SVM (Linear) | **80.0%** | 78.1% |
| Random Forest | **93.3%** | 93.1% |
| MLP | 86.7% | 86.7% |
| SVM (RBF) | 66.7% | 63.1% |
| KNN (k=3) | 66.7% | 64.4% |
| KNN (k=5) | 60.0% | 46.7% |

### Spike Encoder + RF Classifier

| Encoder | Test Accuracy |
|---------|--------------|
| Delta | 60.0% |
| Latency | 40.0% |
| Rate | 20.0% |
| Threshold | 20.0% |
| Population | 20.0% |

### Fixed-Point LSM (retrained readout, fold 2)

| Precision | Accuracy | Δ from float |
|-----------|----------|-------------|
| Float (ref) | 83.9% | — |
| 16-bit Q3.12 | 84.8% | +0.9 pp |
| 12-bit Q3.8 | 83.9% | 0.0 pp |
| 8-bit Q3.4 | 75.2% | −8.7 pp |
| 4-bit Q3.0 | 71.7% | −12.2 pp |

Large ± values are genuine across-fold variance from small dataset (15 sweeps).
Q-values filtered to physically plausible range (5–500) for MEMS in liquid.

---

## Quick Start

```sh
# Full regeneration (single command)
python regenerate_all.py --task high-glucose --window-size 128 --num-seeds 5 --epochs 150

# Or step by step:
python prepare_dataset.py --task high-glucose --split grouped --window-size 128

# Feature extraction (17 features, local-band Q/bw, 15 diagnostic plots)
python notebooks/nb4_feature_extraction.py --task high-glucose

# Feature ML baselines
python notebooks/nb5_feature_ml_baselines.py --task high-glucose

# Neural models (5 seeds × 3 folds = 15 runs each)
python train.py --task high-glucose --folds --model cnn1d --num-seeds 5 --epochs 150 --window-size 128
python train.py --task high-glucose --folds --model spiking_cnn1d --num-seeds 5 --epochs 150 --window-size 128
python train.py --task high-glucose --folds --model temporal_lif_snn --num-seeds 5 --epochs 150 --window-size 128
python train.py --task high-glucose --folds --model rate_snn_mlp --num-seeds 5 --epochs 150 --window-size 128

# Reservoir models (5 seeds × 3 folds)
python notebooks/nb11_reservoir.py --task high-glucose --folds --num-seeds 5 --window-size 128
python notebooks/nb11_reservoir.py --task high-glucose --folds --num-seeds 5 --lsm --window-size 128

# Encoder evaluation
python notebooks/nb9_encoder_evaluation.py --task high-glucose --split grouped

# Model comparison
python notebooks/nb12_model_comparison.py --task high-glucose

# Fixed-point + HDL
python notebooks/nb13_fixed_point_lif.py
python notebooks/nb14_fixed_point_pmut.py --task high-glucose --split grouped --window-size 128
python notebooks/nb15_hdl_test_vectors.py --task high-glucose --split grouped --window-size 128
python notebooks/nb16_hdl_spec.py --generate-hdl

# Central results
python build_central_results.py
```

---

## Project Structure

```
pmut_snn_models/
├── src/pmut_models/       # Core library
│   ├── data.py            # Loading, windowing, 3-fold rotation, phase validation
│   ├── spiking.py         # SNN/CNN models (CNN1D, SpikingCNN1D, TemporalLIFSNN, …)
│   ├── train_utils.py     # Training loop, multi-seed, sweep aggregation, encoder diagnosis
│   ├── reservoir.py       # ESN + LSM (Liquid State Machine)
│   ├── fixed_point.py     # Q-format, FixedPointLIF, IntegerLSM, HDL test vectors
│   └── config.py          # Default paths
├── notebooks/             # Experiment notebooks
│   ├── nb4_feature_extraction.py    # 17 corrected features (local-band Q/bw)
│   ├── nb5_feature_ml_baselines.py  # RF=93.3%, SVM=80.0%, MLP=86.7%, KNN
│   ├── nb8_spike_encoding.py       # Rate/latency/delta/threshold/population encoders
│   ├── nb9_encoder_evaluation.py   # Encoder comparison (RF classifier)
│   ├── nb11_reservoir.py           # ESN + LSM training (3-fold)
│   ├── nb12_model_comparison.py    # Cross-model comparison + pipeline selection
│   ├── nb13_fixed_point_lif.py     # Float vs fixed-point LIF comparison
│   ├── nb14_fixed_point_pmut.py    # Retrained-readout reservoir quantisation
│   ├── nb15_hdl_test_vectors.py    # HDL test vector generation
│   └── nb16_hdl_spec.py            # HDL specification generation
├── outputs/               # Generated results (fold-based layout)
│   ├── datasets/          # Prepared .npz files
│   ├── features/          # NB4: feature table + diagnostic band plots
│   ├── feature_ml/        # NB5: baseline summary + confusion matrices
│   ├── runs/              # Neural models: {task}_folds_w{win}/{model}/fold{N}/
│   ├── reservoir/         # ESN + LSM: {task}/{split}/fold{N}/[lsm/]
│   ├── encoder_evaluation/# NB9: encoder comparison CSV + plots
│   ├── comparison/        # NB12: comparison tables + pipeline selection
│   ├── fixed_point/       # NB13/NB14: bit-width study
│   ├── hdl_test_vectors/  # NB15: CSV + JSON test vectors (16-bit, 12-bit)
│   ├── hdl/               # NB16: HDL spec + Verilog LIF neuron
│   └── central_results/   # Master CSV + JSON (107 rows, 22 columns)
├── regenerate_all.py      # Single-command reproducible regeneration
├── build_central_results.py  # Central results aggregator
├── REPRODUCIBILITY.md     # Frozen commit, data checksums, commands
└── CLAUDE.md              # AI assistant guidance
```

---

## Evaluation Protocol

**3-fold sweep rotation:** Each fold uses a different physical sweep for train/val/test.

| Fold | Train | Val | Test |
|------|-------|-----|------|
| 0 | Sweep 1 | Sweep 2 | Sweep 3 |
| 1 | Sweep 2 | Sweep 3 | Sweep 1 |
| 2 | Sweep 3 | Sweep 1 | Sweep 2 |

**Multi-seed:** 5 seeds `[7, 42, 123, 999, 2024]` per fold = 15 independent runs per model.

**Sweep-level aggregation:** Window predictions are grouped by sweep_key and combined
via mean logits (or majority vote). Feature ML models are natively sweep-level.

---

## Key Design Decisions

- **glucose-ladder (2–20 mM) removed from primary study.** Single-sweep classes cannot
  support independent train/test. Retained in `data.py` for exploratory visualisation.
- **Logistic Regression removed.** Replaced by Random Forest across all evaluation pipelines.
- **Phase preprocessing verified.** Phase carries less discriminative info than amplitude for
  damped PMUT — this is a physical property, not a bug.
- **ESN and LSM perform similarly on the primary benchmark.** ESN 80.6%, LSM membrane
  78.1%, LSM spikes 82.6% window-level.
- **Encoder→SNN yields poor accuracy** due to fundamental information loss from binary
  encoding + single channel + fixed projection.
- **16-bit and 12-bit fixed-point preserve accuracy.** 16-bit Q3.12 achieves 84.8% (vs 83.9%
  float reference). Below 12 bits, degradation becomes significant.

---

## HDL Status

| Deliverable | Status |
|-------------|--------|
| HDL specification | ✅ Complete |
| Verilog LIF neuron (v_next corrected) | ✅ Complete |
| Self-checking testbench | ✅ Built-in sanity test |
| PMUT spike-to-current scaling | ✅ Fixed (binary gate) |
| Test vectors (16-bit, 12-bit) | ✅ Regenerated |
| Multi-neuron reservoir | ❌ Not yet |
| Icarus/Verilator simulation | ❌ Not run |

---

## License

MIT
