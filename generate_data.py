import pandas as pd
import numpy as np

def create_synthetic_health_data(filepath, days=500):
    date_range = pd.date_range(start='2023-01-01', periods=days, freq='D')
    data = pd.DataFrame({
        'date': date_range,
        'flu_cases': np.random.poisson(lam=10, size=days) + np.linspace(0, 50, days).astype(int),
        'dengue_cases': np.random.poisson(lam=3, size=days),
        'mobility_index': np.random.uniform(0.3, 1.0, size=days)
    })
    data.to_csv(filepath, index=False)
    print(f"Synthetic data with {days} rows saved to {filepath}")

if __name__ == "__main__":
    create_synthetic_health_data('health_data.csv')
