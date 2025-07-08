THRESHOLD = 30

def generate_alert(forecast):
    if forecast.max() > THRESHOLD:
        return "🚨 ALERT: Predicted outbreak detected. Consider immediate intervention."
    else:
        return "✅ No significant outbreak predicted in the forecast period."
