# Community Health Outbreak Detection

## Files

- `generate_data.py`: Generates synthetic health data with flu cases, dengue cases, and mobility index.
  - Uses: pandas, numpy

- `data_ingestion.py`: Loads and fills missing health data from CSV.
  - Uses: pandas

- `pattern_detection.py`: Clusters data using KMeans to detect outbreak patterns.
  - Uses: sklearn.cluster.KMeans

- `risk_modeling.py`: Forecasts flu cases using ARIMA model.
  - Uses: statsmodels.tsa.arima.model.ARIMA

- `alerting.py`: Generates alert based on forecasted flu cases.
  - Constant: `THRESHOLD = 30`

- `main.py`: Runs the full process - data loading, clustering, forecasting, and alerting.

## How to Use

1. Run `generate_data.py` to create `health_data.csv`:
   ```bash
   python generate_data.py
