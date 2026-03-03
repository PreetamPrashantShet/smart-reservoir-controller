import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load your dataset
df = pd.read_csv("../integrated_reservoir_dataset_cleaned.csv")

# Select features
features = [
    "storage",
    "rainfall_mm",
    "avg_temperature_c",
    "estimated_inflow"
]

# Create next-day target
df["next_day_storage"] = df["storage"].shift(-1)

df = df.dropna()

X = df[features]
y = df["next_day_storage"]

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "app/models/trained_model.pkl")

print("Model trained successfully.")