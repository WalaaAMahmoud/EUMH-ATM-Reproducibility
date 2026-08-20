# Data Availability

## Primary dataset: NN5

The primary study uses the NN5 daily ATM panel from the Monash Time Series Forecasting Archive.

- Archive record: https://zenodo.org/records/3889740
- Study role: primary controlled benchmark
- Series: 111 ATM time series
- Forecast horizon: 56 days
- Redistribution: users should obtain the dataset from the authoritative archive and comply with its terms.

## External validation dataset

The independent validation panel was obtained from the Kaggle dataset **Data of ATM Transaction of XYZ Bank**.

- Dataset page: https://www.kaggle.com/datasets/nitsbat/data-of-atm-transaction-of-xyz-bank
- Study role: independent five-ATM validation panel
- Raw rows reported in the manuscript: 11,589
- Observed final targets used for scoring: 266
- Redistribution: the raw file is not included in this repository because its licence field was unknown at acquisition. Users must obtain it from the source and verify the current terms.

## Derived artifacts

Only non-sensitive derived artifacts that can be shared lawfully should be deposited. Each derived table or ledger must include:

- source dataset identifier;
- temporal split;
- forecast horizon;
- model and seed;
- preprocessing/configuration hash;
- metric definition; and
- generating script or notebook.

No raw banking data, personal information, credentials, or institution-restricted data should be committed.
