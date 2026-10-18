# Review status — 18 October 2026

This is a local extraction for author review. Nothing was uploaded, committed, retrained or published. Copied research files are byte-for-byte originals. Derived indexes are clearly named. Only the requested pmut_snn_models source tree supplied copied assets; sibling raw data and external manuscript figures were not included.

## Main gaps

- Raw data: the original 15 glucose sweeps and baseline-liquid measurements are missing from this source tree. Original code refers to a separate PMUT-SNN directory.
- Saved NPZ: shapes are training 368 x 128 x 4, validation 92 x 128 x 4, testing 230 x 128 x 4. Training and validation share 10 parent sweeps. This is not the 230/230/230 sweep-separated rotation described in the manuscript. Do not label this NPZ as that benchmark. Use data/splits/saved_npz_group_counts.csv and the separately extracted rotation assignments to inspect the distinction.
- Window provenance: parent groups are saved, but per-window frequency start/end and stable window IDs are not. Do not invent them from normalised arrays.
- Models: only the copied CNN/SpikingCNN PyTorch state_dict checkpoints were found. No fitted physical-feature classifiers, separately saved reservoir matrices, Ridge readouts or precision-specific fitted readouts were found. Available training-only normalisation statistics are in recorded neural metadata.
- Results: class-score columns are absent from inspected prediction CSVs. Central results mix individual runs and summaries; they are not a resolved manuscript results index. Inspect saved JSON before making aggregation claims.
- Decay sensitivity: no dedicated beta sensitivity configurations or result files were found. Do not manufacture the reported study.
- SpikingCNN: this source contains 15 checkpoints across three folds, beyond the email's manuscript scope of fold 0. All are retained under exploratory labels for your decision.
- Precision: bit_width_study.json records the 4-bit format as Qs1.2, whereas the original source README labels it Q3.0. The notebook simulates quantise/dequantise arithmetic with a newly fitted floating-point membrane readout. Confirm split, seed and supporting individual predictions. The summary alone is insufficient to reproduce each precision result from saved fitted models.
- Hardware: test vectors include a ten-neuron software trace (see params.json), not proof that the one-neuron RTL or complete 300-neuron reservoir was simulated successfully. verify_hdl_checklist.py and source central tables make claims that need primary simulation evidence.
- Feature preprocessing: nb5_feature_ml_baselines.py fills missing predictor values with full-table medians in prepare_X_y before cross-validation. Although scaling is inside each fold, imputation is not. Review this possible preprocessing leakage before publication; source code was preserved unchanged.
- Portability: original scripts contain an absolute Windows raw-data default and several hardcoded outputs/ paths. Run scripts/restore_output_layout.py to restore copied original artifacts, then review path arguments and raw data placement. Fresh-checkout end-to-end execution has NOT been validated.
- Requirements pins describe the source folder's current virtual environment, not a proven historical training environment. Missing dependency versions: none for direct requirements.
- Figure 6: no final manuscript-numbered Figure 6 can be identified from this source alone. Existing figures and their scripts were collected; no disputed plot was regenerated or asserted to be final.
- Publication metadata: confirm author names/order and add an agreed license. The draft CITATION.cff uses the new email repository URL. Original README retains older repository and result claims under docs/original/.

## What was checked

Every copied file was SHA-256 checked against its source. Research code and checkpoints were not executed or deserialised. The 15-row feature table, selected 17 predictors, NPZ headers/Unicode metadata and saved run JSON were inspected. Packaging completion is not scientific validation or approval to push.
