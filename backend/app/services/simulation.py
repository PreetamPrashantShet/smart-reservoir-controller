from app.models.ml_model import model_instance
from app.services.optimizer import calculate_release
from app.services.risk_detector import detect_risk


def forecast_15_days(initial_data):

    results = []
    current_storage = initial_data["storage"]
    capacity = initial_data["capacity"]

    rainfall = initial_data["rainfall_mm"]
    temperature = initial_data["avg_temperature_c"]
    inflow = initial_data["estimated_inflow"]

    for day in range(15):

        features = [
            current_storage,
            rainfall,
            temperature,
            inflow
        ]

        predicted_storage = model_instance.predict(features)

        storage_percent = (predicted_storage / capacity) * 100

        release = calculate_release(predicted_storage, capacity, inflow)

        risk, probability = detect_risk(
            predicted_storage,
            capacity,
            rainfall
        )

        results.append({
            "day": day + 1,
            "predicted_storage": round(predicted_storage, 4),
            "storage_percentage": round(storage_percent, 2),
            "recommended_release": round(release, 4),
            "risk_status": risk,
            "flood_probability_percent": probability
        })

        current_storage = predicted_storage - release

    return results