# Reproducibility status — 22 October 2026

The PR-3 S0–S13 code and preserved experiment outputs are provided as eight binary parts in `packages/`; run `python packages/reassemble_package.py` to reconstruct `EUMH_ATM_Thesis_Code_Verified.zip`. The original ZIP is unchanged; its SHA-256 is recorded in `packages/SHA256SUMS`.

The package includes Python and R source, protocol configuration, environment specifications, stage manifests, prediction ledgers, derived tables, figures, tests and execution instructions. See README_AR.md for the supplied verification report and limitations.

## Verification limits

ZIP integrity was checked during deposit. The supplied report records Appendix C agreement (400/400) and saved acceptance gates (404/404 PASS); these are reported historical checks, not a new end-to-end run. Full training and clean-environment reproduction have not been repeated during this deposit. Trained weights and raw datasets are absent. Prophet post-hoc output files are not available. Protocol manifests carry successive amendment hashes; see the supplied report.

Earlier code is separated under archive_superseded inside the package and must not be treated as the PR-3 implementation. Dataset redistribution constraints remain in DATA_AVAILABILITY.md. No new software licence is granted by this deposit.

## Archival status

No Zenodo DOI has been confirmed. Do not cite a placeholder DOI or describe this deposit as fully reproduced. GitHub upload, a versioned release and Zenodo archival publication are distinct steps.
