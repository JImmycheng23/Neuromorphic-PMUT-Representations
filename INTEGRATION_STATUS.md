# GitHub integration status

This branch imports the final Git-paper source/results package and the verified supplement. The original Desktop folder is unchanged. `repository/` contains Git-paper; `generated/` and the root scripts contain recovered-data provenance, regenerated fitted exports and their validation evidence. Run the documented commands from the repository root.

The raw data, regenerated datasets/splits, portable wrappers and fitted exports identified as absent from the original Desktop extraction are now included here. `REQUIREMENTS_AUDIT.md`, `REQUIREMENTS_CHECKED.csv` and `requirements_validation.json` preserve the pre-integration audit and its original folder comparison. They do not imply that this branch lacks those imported files.

Five requirements remain partial: complete acquisition metadata; a unified configuration interface; fresh top-to-bottom execution of all notebook-style scripts; final numbered manuscript/device artwork; and final license/author metadata plus a clean-install check. This PR does not claim all requirements are complete.

SpikingCNN1D reporting remains fold 0 only (five seeds); later saved folds are archival. HDL remains an unverified single-neuron prototype. No new hardware verification or full-reservoir implementation is claimed.

The precision study has separate floating-reference and per-precision supporting outputs in `generated/precision_regeneration/`. Its protocol states splits, seeds, membrane-state representation and window-level evaluation. Ridge is refitted independently for every condition, while preprocessing and readout fitting/scoring remain floating point.

Historical result audits and copied notebook documentation are retained for provenance. The earlier probability-averaging aggregates are distinct from the latest manuscript's majority-vote selection. Regenerated fitted models are labelled as new exports; their validated agreement with archived outputs does not turn them into recovered historical model files. Existing numerical implementations are preserved, with only the two CLI-help changes recorded in `CODE_AMENDMENTS.json`.

`MANIFEST.csv` records the exact bytes of tracked package files except itself. `.gitattributes` disables line-ending conversion so that checksum verification remains meaningful across checkouts.
