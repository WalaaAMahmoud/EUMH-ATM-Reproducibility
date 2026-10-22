# Reproducibility status — 22 October 2026

## Current archival status: completed

Zenodo archival publication is complete for the PR-3 S0–S13 materials and the full S14 computational companion. The complete deposit is **Zenodo version 1.1.1**, published on **22 October 2026**.

- **DOI for the complete deposit:** https://doi.org/10.5281/zenodo.23575850
- **Published record:** https://zenodo.org/records/23575850
- **All-versions DOI:** https://doi.org/10.5281/zenodo.23558921
- **GitHub release containing the S14 asset:** https://github.com/WalaaAMahmoud/EUMH-ATM-Reproducibility/releases/tag/v1.1.0

The complete Zenodo record contains two downloadable files:

| File | Contents | Recorded size |
| --- | --- | --- |
| `WalaaAMahmoud/EUMH-ATM-Reproducibility-v1.1.0.zip` | Repository snapshot, including the original PR-3 S0–S13 package and S14 documentation | Approximately 40.6 MB |
| `Paper2_S14_Computational_Companion.zip` | Complete original S14 computational companion | 115,154,750 bytes |

**Download and extract the S14 ZIP directly.** It is a separate GitHub release asset and a separate Zenodo file; it is not embedded in GitHub's automatically generated source-code ZIP. The earlier proposed S14 split-part reconstruction is not the published distribution method.

Archival publication confirms preservation and availability.

The PR-3 S0–S13 code and preserved experiment outputs are provided as eight binary parts in `packages/`; run `python packages/reassemble_package.py` to reconstruct `EUMH_ATM_Thesis_Code_Verified.zip`. The original ZIP is unchanged; its SHA-256 is recorded in `packages/SHA256SUMS`.

The package includes Python and R source, protocol configuration, environment specifications, stage manifests, prediction ledgers, derived tables, figures, tests and execution instructions. See README_AR.md for the supplied verification report and limitations.

## Verification limits

ZIP integrity was checked during deposit. The supplied report records Appendix C agreement (400/400) and saved acceptance gates (404/404 PASS); these are reported historical checks. Trained weights and raw datasets are absent from the original PR-3 package; the separate S14 companion includes the supplied NN5 input files, as noted below. Prophet post-hoc output files are not available. Protocol manifests carry successive amendment hashes; see the supplied report.

Earlier code is separated under archive_superseded inside the package and must not be treated as the PR-3 implementation. Dataset redistribution constraints remain in DATA_AVAILABILITY.md. The Zenodo archive metadata lists CC BY 4.0. No separate source-code licence file is included.

## Original PR-3 archive (version history)

Version v1.0.0 was published on GitHub on 22 October 2026 at commit 85c6b599bcea75e7372c3f6763572c08c7f023d5 and archived by Zenodo.

- Version DOI: https://doi.org/10.5281/zenodo.23558922
- All-versions DOI: https://doi.org/10.5281/zenodo.23558921
- Release: https://github.com/WalaaAMahmoud/EUMH-ATM-Reproducibility/releases/tag/v1.0.0

All eight uploaded part sizes and Git blob hashes match the local parts; their reassembly was verified against the original ZIP SHA-256.

## S14 addition in v1.1.0

The supplied S14 computational companion has 255 files and is deposited byte-for-byte as the complete `Paper2_S14_Computational_Companion.zip` release asset. ZIP integrity and Python syntax (35 files) were checked. Follow packages/s14/README_S14.md for dependencies, source/portable-script distinctions, overlapping origins, calibration boundaries and recorded numerical verification mismatches. The S14 package includes supplied NN5 raw inputs; secondary transaction data and fitted weights are absent.

The complete S14 companion is published as the GitHub v1.1.0 release asset and as a separate file in Zenodo v1.1.1, DOI https://doi.org/10.5281/zenodo.23575850. Zenodo v1.1.1 also retains the PR-3 repository archive. The earlier automatic Zenodo v1.1.0 archive contains only repository files and lacks the S14 binary. GitHub reports the original S14 SHA-256 72dc8d76161fc6b3559b0f935908747e189236095a27c5366c75085460a4e9b6; Zenodo records MD5 eb80c12245484d67bf7475916d0db330.
