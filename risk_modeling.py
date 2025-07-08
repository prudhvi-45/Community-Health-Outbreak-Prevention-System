# risk_modeling.py
from statsmodels.tsa.arima.model import ARIMA

def forecast_flu_cases(df, steps=7):
    series = df['flu_cases']
    model = ARIMA(series, order=(1,1,1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=steps)
    return forecast
