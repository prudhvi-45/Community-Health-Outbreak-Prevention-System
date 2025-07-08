# Community Health Outbreak Prevention System

This project is an early warning system to detect and prevent disease outbreaks in a community using synthetic health data and machine learning techniques.

## Features

- Generates synthetic health data (flu, dengue, mobility)
- Detects potential outbreak clusters using KMeans
- Forecasts future flu cases with ARIMA
- Triggers alerts if outbreak thresholds are exceeded

## Project Structure

- `generate_data.py`: Creates synthetic health data (`health_data.csv`)
- `data_ingestion.py`: Loads and prepares the data
- `pattern_detection.py`: Clusters data to detect outbreak patterns
- `risk_modeling.py`: Predicts future flu cases
- `alerting.py`: Generates alerts based on forecasted data
- `main.py`: Runs the full pipeline

## How to Run

1. Generate data:
   ```bash
   python generate_data.py
