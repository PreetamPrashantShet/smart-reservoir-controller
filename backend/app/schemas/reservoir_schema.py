from pydantic import BaseModel

class ForecastInput(BaseModel):
    storage: float
    capacity: float
    rainfall_mm: float
    avg_temperature_c: float
    estimated_inflow: float