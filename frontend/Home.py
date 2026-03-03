import streamlit as st
import random
import pandas as pd
import plotly.graph_objects as go
import time

st.set_page_config(page_title="15-Day Reservoir Forecast", layout="wide")

st.title("🌊 15-Day Reservoir Prediction")

# -----------------------------
# INPUT SECTION
# -----------------------------
storage = st.number_input("Current Storage", value=0.8)
capacity = st.number_input("Reservoir Capacity", value=1.5)
rainfall = st.number_input("Rainfall (mm)", value=120.0)
temperature = st.number_input("Temperature (°C)", value=32.0)
inflow = st.number_input("Estimated Inflow", value=0.3)

run_button = st.button("Run AI Prediction")

# -----------------------------
# SMS SIMULATION FUNCTION
# -----------------------------
def send_sms_simulation(message):
    st.toast("📱 SMS Alert Sent!")
    st.info(f"SMS Message: {message}")

# -----------------------------
# PREDICTION SECTION
# -----------------------------
if run_button:

    with st.spinner("Running AI Simulation..."):
        time.sleep(1)

        base_storage = storage * 100
        forecast_data = []

        for day in range(1, 16):
            change = random.uniform(-3, 6)
            base_storage += change

            flood_probability = random.randint(10, 95)

            if flood_probability > 80:
                risk = "Severe Flood Risk"
            elif flood_probability > 60:
                risk = "Flood Risk"
            elif flood_probability < 30:
                risk = "Water Scarcity Risk"
            else:
                risk = "Safe"

            forecast_data.append({
                "Day": day,
                "Predicted Storage": round(base_storage, 2),
                "Flood Probability (%)": flood_probability,
                "Risk Status": risk
            })

        df = pd.DataFrame(forecast_data)

    st.markdown("---")
    st.subheader("📈 Forecast Analysis")

    colA, colB, colC = st.columns(3)

    final_storage = df.iloc[-1]["Predicted Storage"]
    final_prob = df.iloc[-1]["Flood Probability (%)"]
    final_risk = df.iloc[-1]["Risk Status"]

    colA.metric("Final Storage", final_storage)
    colB.metric("Flood Probability", f"{final_prob}%")
    colC.metric("Risk Status", final_risk)

    # GRAPH
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Day"],
        y=df["Predicted Storage"],
        mode="lines+markers",
        line=dict(width=3),
        name="Predicted Storage"
    ))

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Day",
        yaxis_title="Storage Level",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

    # TABLE
    st.subheader("📋 15-Day Detailed Forecast Table")
    st.dataframe(df, use_container_width=True)

    # SMS ALERT
    if "Severe" in final_risk:
        send_sms_simulation(
            f"🚨 Severe Flood Risk! Predicted Storage: {final_storage}"
        )
    elif "Flood" in final_risk:
        send_sms_simulation(
            f"⚠ Flood Risk Warning! Probability: {final_prob}%"
        )