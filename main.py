from data_ingestion import load_health_data
from pattern_detection import detect_outbreak_clusters
from risk_modeling import forecast_flu_cases
from alerting import generate_alert

def main():
    df = load_health_data('health_data.csv')
    print("Data loaded successfully.")

    df = detect_outbreak_clusters(df)
    print("\nCluster assignments (0=low risk, 1=high risk):")
    print(df[['date', 'flu_cases', 'dengue_cases', 'cluster']].tail(10))

    forecast = forecast_flu_cases(df)
    print("\nForecasted flu cases for next 7 days:")
    print(forecast)

    alert = generate_alert(forecast)
    print("\n" + alert)

if __name__ == "__main__":
    main()
