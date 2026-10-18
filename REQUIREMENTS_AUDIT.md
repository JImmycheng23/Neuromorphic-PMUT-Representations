> **Pre-integration audit snapshot (18 October 2026).** References below to missing items in the Desktop Git-paper folder describe the original extraction before this pull request. This GitHub branch integrates the assembled package; see [current integration status](INTEGRATION_STATUS.md). Remaining partial scientific/documentation requirements are retained.

# Requirements coverage audit — 18 October 2026

Basis: the 14 rows of `Git-paper/docs/REQUIREMENTS_CHECKLIST.csv`. This is an audit of those declared requirements, not a certification of every scientific implementation or an expansion of the study scope.

## Outcome

The assembled supplement covers the main raw-data, processed-data, split, source, script, model and result deliverables. **It is not accurate to say that every requirement is fully complete, or that the target Git-paper folder already contains the assembled supplement.**

The target folder remains the earlier extraction: its raw measurements, regenerated fitted exports and portable reproduction/inference entry points have not been integrated. Its checklist still labels recovered items as missing. No `.git` directory was found there, so it is not currently a local Git checkout.

## Row-by-row findings

| Requirement | Supplement status | Verified evidence | Remaining gap / target difference |
|---|---|---|---|
| data/raw | Covered | Three original files hash-verified in repository/data/raw. | Target folder still contains raw-data placeholders. |
| data/metadata | Partial | Sweep inventory, classes, 690 frequency-traceable window records and degree/IQ audit supplied. | Drive-voltage convention, temperature and full acquisition record still require author input. |
| data/processed | Covered | Selected features and three 230/230/230 rotation NPZ files regenerated and checked; archived grouped NPZ retained separately. | Generated rotation data are in the supplement, not yet integrated into target. |
| data/splits | Covered | 2070 window/fold assignments, feature-CV assignments and precision split row-to-window IDs supplied. | Target has only the older extracted neural rotation manifest. |
| src | Covered with limitations | Core implementation and six feature classifiers are present; every Python source parses. | Code is preserved for reproducibility; implementation findings are documented separately, not certified absent. |
| configs | Partial | Recorded neural settings, feature bands, reservoir export parameters and per-precision protocols are available. | A unified standalone config-driven training interface is not supplied. No decay-sensitivity experiment is claimed. |
| notebooks | Partial | Eleven numbered Python notebook-style scripts are included; selected command entry points import and expose help. | They are .py scripts; all original notebooks have not been run top-to-bottom in a fresh portable environment. |
| scripts | Covered in supplement | Six-stage reproduction wrapper and saved-reservoir inference entry point are present and import successfully. | These are at supplement root; target Git-paper/scripts still contains only the old restoration helper. |
| models | Covered in supplement | 104 indexed artifacts: 30 original neural checkpoints and 74 regenerated fitted exports; validation records present. | Target still has the 30 original checkpoints without regenerated fitted exports. SpikingCNN reporting is fold 0 only. |
| results | Covered with scope | Per-run metrics, probabilities, precision-specific supporting outputs and explicit reporting scope are supplied. | Archived extra folds are not reported as completed studies. Latest-paper majority-vote review is a separate workspace audit. |
| figures | Partial | Existing plots, plotting source and model results are included. | Final numbered manuscript figures and editable device artwork are not assembled under this code package. |
| hardware | Covered for prototype scope | Single-neuron RTL draft, specification and 12/16-bit software test vectors are present. | Prototype is unverified and has static RTL findings. Full-reservoir hardware is outside the agreed requirement; artifact coverage does not certify working RTL. |
| docs | Covered in supplement | Main README, study scope, precision protocol, provenance and checksum manifest are supplied. | The current staged checklist is updated; the target folder still has the pre-recovery checklist. |
| root metadata | Partial | README, dependency snapshot, .gitignore and draft CITATION.cff are supplied. | License choice and final author/affiliation metadata remain unconfirmed; clean-install validation was not performed. |

## Checks performed

- Parsed all 28 packaged Python files successfully.
- Checked imports and `--help` for 12 entry points: 12 passed. This does not claim that every training workflow was rerun.
- Verified all three raw-file hashes and the supplemental ZIP checksum manifest.
- Checked the saved validation evidence for 33 reservoir runs, 30 neural checkpoint inference checks, five precision conditions and 69 reloaded feature/reservoir exports.
- Checked 104 model-index paths and the ten archival-only SpikingCNN checkpoints. Reported SpikingCNN scope remains fold 0 only.
- Confirmed data-validation records for 15 sweeps, 90000 samples, 690 windows and 2070 fold/window assignments.
- Compared required deliverables with the target folder rather than assuming that building a ZIP had updated that folder.

Detailed machine-readable evidence: `requirements_validation.json`. Updated coverage matrix: `REQUIREMENTS_CHECKED.csv`.

Two staged CLI help corrections fixed prepare_dataset.py and train.py: their percent-containing help strings failed argparse formatting and described the wrong default stride. Both now pass --help. CODE_AMENDMENTS.json records the help-only changes; no model calculation or archived metric changed.

## Before describing the target repository as complete

Integrate the verified source/data/generated exports and portable wrappers into the intended repository layout; update the stale checklist and documentation; add the final manuscript figure assets where required; confirm publication metadata and licensing. Preserve the current explicit precision protocol, fold-0-only SpikingCNN scope and single-neuron HDL scope. Existing implementation caveats must remain documented rather than being treated as passed tests.
