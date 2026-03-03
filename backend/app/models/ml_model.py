import joblib
import pandas as pd

MODEL_PATH = "app/models/trained_model.pkl"

class StorageModel:

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

        self.feature_names = [
            "storage",
            "rainfall_mm",
            "avg_temperature_c",
            "estimated_inflow"
        ]

    def predict(self, features):
        df = pd.DataFrame([features], columns=self.feature_names)
        return self.model.predict(df)[0]

    def get_feature_importance(self):
        importance = self.model.feature_importances_
        return dict(zip(self.feature_names, importance))

    def get_model_info(self):
        return {
            "model_type": "Random Forest Regressor",
            "n_features": len(self.feature_names),
            "features_used": self.feature_names
        }

model_instance = StorageModel()