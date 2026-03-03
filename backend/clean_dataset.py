import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("../data/integrated_reservoir_dataset_2025_26.csv")

print("Original Shape:", df.shape)

# -------------------------------------------------
# 1️⃣ Remove Duplicates
# -------------------------------------------------
df = df.drop_duplicates()

# -------------------------------------------------
# 2️⃣ Remove Rows with Critical Missing Values
# -------------------------------------------------
critical_columns = [
    "storage",
    "live_capacity_frl",
    "rainfall_mm",
    "avg_temperature_c",
    "estimated_inflow"
]

df = df.dropna(subset=critical_columns)

# -------------------------------------------------
# 3️⃣ Fill Minor Missing Values (Optional Columns)
# -------------------------------------------------
df["rainfall_last_3_days"] = df["rainfall_last_3_days"].fillna(0)

# -------------------------------------------------
# 4️⃣ Remove Negative or Invalid Values
# -------------------------------------------------
df = df[df["storage"] >= 0]
df = df[df["rainfall_mm"] >= 0]
df = df[df["estimated_inflow"] >= 0]

# -------------------------------------------------
# 5️⃣ Fix Data Types
# -------------------------------------------------
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["year"] = df["year"].astype(int)
df["month"] = df["month"].astype(int)

# -------------------------------------------------
# 6️⃣ Remove Extreme Outliers (Optional but Recommended)
# -------------------------------------------------
df = df[df["storage"] <= df["live_capacity_frl"] * 1.2]

# -------------------------------------------------
# 7️⃣ Recalculate Storage Percentage
# -------------------------------------------------
df["storage_percentage"] = (
    df["storage"] / df["live_capacity_frl"] * 100
)

# -------------------------------------------------
# Save Cleaned Dataset
# -------------------------------------------------
df.to_csv("../integrated_reservoir_dataset_cleaned.csv", index=False)

print("Cleaned Shape:", df.shape)
print("Dataset cleaned successfully.")