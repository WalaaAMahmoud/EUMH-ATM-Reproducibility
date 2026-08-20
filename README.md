# EUMH-ATM Reproducibility Repository

This repository supports the paper:

**EUMH-ATM: An Explainable and Uncertainty-Aware Multi-Hybrid AI Framework for ATM Cash Management with Downstream Sustainability Evaluation**

## Study scope

EUMH-ATM is an end-to-end, forecast-to-decision research pipeline integrating:

1. leakage-safe multi-horizon ATM cash-demand forecasting;
2. statistical, machine-learning, hybrid, and Transformer benchmarks;
3. model-specific explainability using Integrated Gradients and TreeSHAP;
4. uncertainty quantification using quantile, conformal, CQR, and MC Dropout approaches;
5. replenishment-policy evaluation; and
6. routing-based scenario evaluation of distance and estimated CO2e.

The primary experiment uses 111 NN5 ATM series with a 56-day horizon, five prespecified seeds, rolling-origin development, a registered pre-final window, and a once-only final holdout. A separate five-ATM transaction panel is used for external validation.

## Repository status

The repository is public and has been initialized for archival integration. The following metadata and documentation are currently available:

- citation metadata;
- Zenodo deposition metadata;
- dataset availability and redistribution constraints;
- a transparent reproducibility-status register; and
- eight recent references (2024–2025) linked to the paper.

**Important:** executable source code, frozen configurations, prediction ledgers, experiment-registry exports, and derived result tables have not yet been deposited in this repository. They must be uploaded and checked before a versioned reproducibility release is created. No DOI should be cited until Zenodo has archived an actual GitHub release.

## Intended release structure

```text
config/                Frozen experiment configurations
src/                   Preprocessing, forecasting, XAI, UQ, policy and routing code
scripts/               Reproduction entry points
results/               Derived, non-sensitive result tables and ledgers
docs/                  Protocol and artifact documentation
references/            Bibliographic metadata
```

## Data

- NN5 daily ATM dataset: [Monash Time Series Forecasting Archive on Zenodo](https://zenodo.org/records/3889740)
- External five-ATM panel: [ATM transaction data of XYZ Bank on Kaggle](https://www.kaggle.com/datasets/nitsbat/data-of-atm-transaction-of-xyz-bank)

The external raw file is not redistributed here because its licence field was unknown at acquisition. See [DATA_AVAILABILITY.md](DATA_AVAILABILITY.md).

## Authors

- Walaa Adel Mahmoud Mohamed
- Mohamed Abu Rizka
- Khaled Mahar
- Mohammed Abdelsalam

## Citation and DOI

Citation metadata are provided in [CITATION.cff](CITATION.cff). A DOI will be added only after an auditable versioned release is archived by Zenodo.

## Contact

For academic queries and controlled access to materials that cannot yet be redistributed, please contact the corresponding author through the manuscript submission record.
