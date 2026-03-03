from fastapi import APIRouter
from app.schemas.reservoir_schema import ForecastInput
from app.services.simulation import forecast_15_days
from app.models.ml_model import model_instance

router = APIRouter()

# Health check
@router.get("/")
def root():
    return {"message": "Smart Reservoir Controller API Running"}

# 15-day Forecast
@router.post("/forecast-15-days")
def forecast(data: ForecastInput):
    results = forecast_15_days(data.dict())
    return {"forecast": results}

# Feature importance
@router.get("/model/feature-importance")
def feature_importance():
    return model_instance.get_feature_importance()

# Model info
@router.get("/model/info")
def model_info():
    return model_instance.get_model_info()