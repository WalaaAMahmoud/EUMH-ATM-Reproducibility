# Paper 2 post-review computational companion

This package supports the additional results in the NCA manuscript. It contains
nine complete H=56 origin evaluations, a separate fitted-weight holdout interval
sensitivity, cash-only scenario records, original helpers and the necessary NN5
input features and reference ledgers. It does not contain original fitted model
weights and does not claim reproduction of all old predictions.

## Scope

Origins: 679, 686, 693, 700, 707, 714, 721, 728, 735.
Primary refit target ceiling: 679; frozen settings and five registered seeds.
Calibration sensitivity target ceiling: 623; calibration targets: 624–679;
one seed; identical weights are kept for calibration and all later origins.
The old hyperparameter selection includes the calibration period. This is a
holdout from weight fitting, not from model selection. Adjacent tasks overlap
for 49 days and reuse previously inspected data. No new independent-origin
significance test or untouched-confirmation claim is made.

## Read without rerunning models

`run/s14_summary_models.csv`: main Table 3.
`run/s14_summary_by_origin.csv`: Fig. 6 and supplementary Table S14.
`run/s14_calibration_aggregate.csv`: supplementary Table S15.
`run/s14_numerical_verification.csv`: supplementary Table S16.
`run/s14_results/*.csv.gz`: full point predictions, observed masks and keys.
`run/s14_calibration/*.csv.gz`: full intervals and target masks.
`run/s14_calibration/cash_simulation_sensitivity.csv`: all cash-only settings.
The cash table keeps both calendar-denominator and observed-day service.
Neither convention recovers missing demand or its balance effect.

## Recompute summaries

Use a Python 3.12 environment and the recorded numerical dependencies. The
`requirements_s14.txt` file covers the new evaluation. For a CPU reproduction,
install the CPU build of the recorded PyTorch version. The original manifests
record a different Python and PyTorch binary environment; numerical prediction
identity should be checked, not assumed.

From the unpacked package root:

    python scripts/summarize_s14.py
    python scripts/recompute_cash_sensitivity.py

## Refit the new tasks

    python scripts/rebuild_features.py
    python scripts/evaluate_multi_origin.py cnn_lstm

Repeat the last command for lstm, tft, patchtst, fusion_c1_neural, c1_no_cnn,
c1_no_xgb and snaive7. The fusion fits include a computationally costly frozen
tree cross-fitting stage. New output replaces the corresponding local result
file, so keep a copy of the supplied execution before rerunning.

For the separate calibration experiment:

    python scripts/evaluate_calibration_sensitivity.py cnn_lstm
    python scripts/evaluate_calibration_sensitivity.py lstm
    python scripts/evaluate_calibration_sensitivity.py tft
    python scripts/summarize_s14.py
    python scripts/recompute_cash_sensitivity.py

The portable scripts resolve their paths relative to this package. The
`executed_sources` directory preserves the source scripts from the review
workspace, including their original absolute paths. No modified portable
script is presented as a newly executed model run.

The original code modules, stage records, configuration and necessary ledgers
are retained in `run`. Secondary raw transaction data are not redistributed.
The source protocol and stage hashes are version-specific. S14 is a separate
post-review extension and does not retroactively preregister its analyses.

PatchTST meets the recorded 1e-5 normalised reproduction tolerance at origin 679.
Several recurrent and fusion refits do not. Runtime differences and checked
source hashes are recorded, but the numerical cause has not been isolated.
Original and added results are kept separate in the manuscript.

Cash scenarios use the source cassette-swap simulator. No new route or
emissions simulation accompanies the corrected calibration sensitivity.
