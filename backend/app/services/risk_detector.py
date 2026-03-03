def detect_risk(predicted_storage, capacity, rainfall):

    percent = (predicted_storage / capacity) * 100

    # Base flood probability based on storage %
    if percent >= 95:
        flood_probability = 90
    elif percent >= 90:
        flood_probability = 70
    elif percent >= 80:
        flood_probability = 40
    else:
        flood_probability = 10

    # Increase probability if heavy rainfall
    if rainfall > 120:
        flood_probability += 10

    flood_probability = min(flood_probability, 100)

    # Decide risk label
    if flood_probability >= 80:
        risk_status = "Severe Flood Risk"
    elif flood_probability >= 60:
        risk_status = "Flood Warning"
    elif percent <= 30:
        risk_status = "Water Scarcity Risk"
    else:
        risk_status = "Normal"

    return risk_status, flood_probability