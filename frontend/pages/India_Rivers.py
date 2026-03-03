import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

API_URL = "http://127.0.0.1:8000"

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="National Water Intelligence System",
    layout="wide",
    page_icon="🌊"
)

# -----------------------------
# HEADER
# -----------------------------
st.title("🇮🇳 National Water Intelligence Command Center")
st.caption("AI Powered Reservoir Monitoring & Flood Risk Analytics")
st.markdown("---")

# -----------------------------
# RIVER MASTER DATA
# -----------------------------
river_data = {
    "Ganga": {"lat": 25.3, "lon": 83.0, "storage": 1.0, "capacity": 2.0, "rainfall": 150, "temp": 30, "inflow": 0.5},
    "Krishna": {"lat": 16.5, "lon": 80.6, "storage": 0.8, "capacity": 1.5, "rainfall": 120, "temp": 32, "inflow": 0.3},
    "Godavari": {"lat": 19.9, "lon": 79.3, "storage": 0.9, "capacity": 1.8, "rainfall": 140, "temp": 31, "inflow": 0.4},
    "Cauvery": {"lat": 11.2, "lon": 78.9, "storage": 0.6, "capacity": 1.2, "rainfall": 100, "temp": 33, "inflow": 0.25},
    "Narmada": {"lat": 22.3, "lon": 77.9, "storage": 0.7, "capacity": 1.4, "rainfall": 110, "temp": 29, "inflow": 0.3},
    "Brahmaputra": {"lat": 26.2, "lon": 91.7, "storage": 1.2, "capacity": 2.2, "rainfall": 200, "temp": 28, "inflow": 0.7}
}

map_data = []
severe = 0
flood = 0
safe = 0

# -----------------------------
# FETCH DATA FROM BACKEND
# -----------------------------
st.markdown("### 🔄 Processing National Risk Data")

with st.spinner("Contacting AI Engine..."):

    for river, data in river_data.items():

        payload = {
            "storage": data["storage"],
            "capacity": data["capacity"],
            "rainfall_mm": data["rainfall"],
            "avg_temperature_c": data["temp"],
            "estimated_inflow": data["inflow"]
        }

        try:
            response = requests.post(f"{API_URL}/forecast-15-days", json=payload, timeout=5)

            if response.status_code == 200:

                df = pd.DataFrame(response.json()["forecast"])
                final_risk = df.iloc[-1]["risk_status"]

                # Risk classification
                if final_risk == "Severe Flood Risk":
                    color = "red"
                    severe += 1

                elif "Flood" in final_risk:
                    color = "orange"
                    flood += 1

                else:
                    color = "green"
                    safe += 1

                map_data.append({
                    "River": river,
                    "Latitude": data["lat"],
                    "Longitude": data["lon"],
                    "Risk": final_risk,
                    "Severity": color
                })

            else:
                st.error(f"Backend error for {river}")

        except requests.exceptions.RequestException:
            st.error(f"AI Engine unreachable for {river}")

# Convert to dataframe
map_df = pd.DataFrame(map_data)

# -----------------------------
# KPI SECTION
# -----------------------------
st.markdown("### 📊 National Risk Overview")

col1, col2, col3 = st.columns(3)

col1.metric("🚨 Severe Zones", severe)
col2.metric("⚠ Flood Warning", flood)
col3.metric("✅ Safe Basins", safe)

st.markdown("---")

# -----------------------------
# MAP SECTION
# -----------------------------
st.markdown("### 🗺 Geospatial Flood Intelligence Map")

if not map_df.empty:

    fig = px.scatter_geo(
        map_df,
        lat="Latitude",
        lon="Longitude",
        color="Severity",
        hover_name="River",
        hover_data=["Risk"],
        color_discrete_map={
            "red": "red",
            "orange": "orange",
            "green": "green"
        },
        scope="asia"
    )

    fig.update_geos(
        center={"lat": 22, "lon": 80},
        projection_scale=4,
        showcountries=True,
        countrycolor="gray"
    )

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("No data available from AI Engine.")

st.markdown("---")
st.caption("© 2026 National Water Intelligence System | Powered by FastAPI + ML Engine")