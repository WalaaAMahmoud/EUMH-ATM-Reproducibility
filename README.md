# EUMH-ATM PR-3 thesis implementation and preserved outputs

This deposit contains the supplied PR-3 S0–S13 implementation package, including Python/R source, protocol configurations, environment specifications, stage manifests, prediction ledgers, derived tables, figures and tests.

## Download and extract

The original 41,011,688-byte ZIP is stored in eight binary parts to accommodate the upload channel. Download or clone this entire repository, then run:

```bash
python packages/reassemble_package.py
```

The script rebuilds `packages/EUMH_ATM_Thesis_Code_Verified.zip` and checks its SHA-256 against the original. Extract that ZIP and follow the enclosed README.md and SETUP.md. No package contents were edited.

See [Arabic guide](README_AR.md), [verification status](REPRODUCIBILITY_STATUS.md), and [data restrictions](DATA_AVAILABILITY.md).

## Verification limits

ZIP integrity and byte-identical reconstruction were checked during deposit. The supplied report describes agreement with saved thesis tables and historical acceptance gates. Trained weights and raw datasets are absent. Earlier implementations remain in archive_superseded and are distinct from PR-3.

## Authors

Walaa Adel Mahmoud Mohamed; Mohamed Abu Rizka; Khaled Mahar; Mohammed Abdelsalam.

## Citation

Version 1.0.0 is archived at https://doi.org/10.5281/zenodo.23558922. The DOI for all versions is https://doi.org/10.5281/zenodo.23558921. See CITATION.cff. The Zenodo archive metadata lists CC BY 4.0; no separate source-code licence file is included.

## S14 post-review computational companion

Version 1.1.0 adds the supplied `Paper2_S14_Computational_Companion.zip` without modifying its contents. Download the complete ZIP from the **Assets** section of [release v1.1.0](https://github.com/WalaaAMahmoud/EUMH-ATM-Reproducibility/releases/tag/v1.1.0) and extract it directly. The repository source archive contains the documentation; the S14 binary companion is a separate release asset.

See [S14 instructions and methodological boundaries](packages/s14/README_S14.md). S14 contains nine overlapping H=56 origin evaluations, a separate fitted-weight holdout calibration sensitivity, cash-only scenarios, portable scripts, executed sources and saved outputs. It does not supply fitted weights or establish untouched confirmation or new independent-origin significance. No new route/emissions simulation is claimed. Saved numerical verification reports include refit mismatches for several models.

The S14 ZIP integrity and syntax of its 35 Python files were checked during deposit. Original package SHA-256: `72dc8d76161fc6b3559b0f935908747e189236095a27c5366c75085460a4e9b6`.

## Complete S14 archive DOI

The complete archive (PR-3 source ZIP plus the original S14 ZIP) is published as Zenodo version 1.1.1: https://doi.org/10.5281/zenodo.23575850. Download S14 directly from that record or the GitHub v1.1.0 release asset. S14 is not included in GitHub's automatically generated source-code ZIP. Do not use the earlier Zenodo v1.1.0 record as evidence of an archived S14 binary.
