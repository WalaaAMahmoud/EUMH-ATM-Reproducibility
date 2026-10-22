# Reproducibility status — 22 October 2026

The PR-3 S0–S13 code and preserved experiment outputs are provided as eight binary parts in `packages/`; run `python packages/reassemble_package.py` to reconstruct `EUMH_ATM_Thesis_Code_Verified.zip`. The original ZIP is unchanged; its SHA-256 is recorded in `packages/SHA256SUMS`.

The package includes Python and R source, protocol configuration, environment specifications, stage manifests, prediction ledgers, derived tables, figures, tests and execution instructions. See README_AR.md for the supplied verification report and limitations.

## Verification limits

ZIP integrity was checked during deposit. The supplied report records Appendix C agreement (400/400) and saved acceptance gates (404/404 PASS); these are reported historical checks, not a new end-to-end run. Full training and clean-environment reproduction have not been repeated during this deposit. Trained weights and raw datasets are absent. Prophet post-hoc output files are not available. Protocol manifests carry successive amendment hashes; see the supplied report.

Earlier code is separated under archive_superseded inside the package and must not be treated as the PR-3 implementation. Dataset redistribution constraints remain in DATA_AVAILABILITY.md. The Zenodo archive metadata lists CC BY 4.0. No separate source-code licence file is included.

## Archival status

Version v1.0.0 was published on GitHub on 22 October 2026 at commit 85c6b599bcea75e7372c3f6763572c08c7f023d5 and archived by Zenodo.

- Version DOI: https://doi.org/10.5281/zenodo.23558922
- All-versions DOI: https://doi.org/10.5281/zenodo.23558921
- Release: https://github.com/WalaaAMahmoud/EUMH-ATM-Reproducibility/releases/tag/v1.0.0

All eight uploaded part sizes and Git blob hashes match the local parts; their reassembly was verified against the original ZIP SHA-256. Archival publication does not establish a new end-to-end reproduction.
