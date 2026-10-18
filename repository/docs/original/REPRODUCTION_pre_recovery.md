# Original workflow and current limits

Original entry points are kept at the root; reusable code is in src/ and numbered scripts in notebooks/. Original research code is unchanged. See docs/original/REPRODUCIBILITY.md for the supplied command sequence and docs/STATUS.md for qualifications.

1. Review docs/REQUIREMENTS_CHECKLIST.csv, models/MODEL_INDEX.csv and docs/COPY_MANIFEST.csv.
2. If running original plotting/analysis commands, run `python scripts/restore_output_layout.py` from the repository root. This materialises copied artifacts at their original outputs/ paths, without overwriting differing files.
3. Review the current-environment dependency pins. Install dependencies in your chosen environment.
4. Add the original raw data and review --data-root arguments / src/pmut_models/config.py. Data have not been copied from outside the requested source folder.
5. Use source entry points after reviewing their arguments. The saved rotation uses 128-sample non-overlapping windows; do not assume every source script's default stride implements this (prepare_dataset.py defaults to half-window stride).

Illustrative source commands (not run or certified by this extraction):

```sh
python prepare_dataset.py --task high-glucose --split grouped --window-size 128 --stride 128 --data-root data/raw
python notebooks/nb4_feature_extraction.py --task high-glucose
python notebooks/nb5_feature_ml_baselines.py --task high-glucose
python train.py --task high-glucose --folds --model cnn1d --num-seeds 5 --epochs 150 --window-size 128
python notebooks/nb11_reservoir.py --task high-glucose --folds --num-seeds 5 --window-size 128
python notebooks/nb11_reservoir.py --task high-glucose --folds --num-seeds 5 --lsm --window-size 128
python notebooks/nb14_fixed_point_pmut.py --task high-glucose --split grouped --window-size 128
python build_central_results.py
```

The grouped NPZ command above does not generate the separate three-fold rotation. Review build_dataset_folds and run metadata. Do not run training solely to populate missing evidence without first resolving manuscript scope.
