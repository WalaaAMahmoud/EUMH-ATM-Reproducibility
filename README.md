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

ZIP integrity and byte-identical reconstruction were checked during deposit. Full training and clean-environment reproduction were not rerun. The supplied report describes agreement with saved thesis tables and historical acceptance gates. Trained weights and raw datasets are absent. Earlier implementations remain in archive_superseded and are distinct from PR-3.

## Authors

Walaa Adel Mahmoud Mohamed; Mohamed Abu Rizka; Khaled Mahar; Mohammed Abdelsalam.

## Citation

Version 1.0.0 is archived at https://doi.org/10.5281/zenodo.23558922. The DOI for all versions is https://doi.org/10.5281/zenodo.23558921. See CITATION.cff. The Zenodo archive metadata lists CC BY 4.0; no separate source-code licence file is included.
