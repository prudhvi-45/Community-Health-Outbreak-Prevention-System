# data_ingestion.py
import pandas as pd

def load_health_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['date'])
    df.fillna(0, inplace=True)
    return df
