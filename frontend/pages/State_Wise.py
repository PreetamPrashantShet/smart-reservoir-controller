import streamlit as st
import random
import pandas as pd
import plotly.graph_objects as go
import time

st.set_page_config(layout="wide")

st.title("🏞 State Wise Reservoir Prediction")

# -----------------------------
# STATE DATA (Demo Structure)
# -----------------------------
state_reservoirs = {
    "Tamil Nadu": ["Mettur Dam", "Bhavani Sagar", "Vaigai Dam"],
    "Karnataka": ["Krishna Raja Sagara", "Almatti Dam"],
    "Gujarat": ["Sardar Sarovar"],
    "Maharashtra": ["Koyna Dam", "Jayakwadi Dam"]
}

# -----------------------------
# SELECT STATE
# -----------------------------
selected_state = st.selectbox("Select State", list(state_reservoirs.keys()))

# -----------------------------
# SELECT RESERVOIR
# -----------------------------
selected_reservoir = st.selectbox(
    "Select Reservoir",
    state_reservoirs[selected_state]
)

st.success(f"Showing reservoir analytics for {selected_reservoir}")

# -----------------------------
# INPUT PARAMETERS
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    storage = st.number_input("Current Storage", value=0.8)
    rainfall = st.number_input("Rainfall (mm)", value=120.0)

with col2:
    capacity = st.number_input("Reservoir Capacity", value=1.5)
    temperature = st.number_input("Temperature (°C)", value=32.0)

run_button = st.button("Run 15-Day Forecast")

# -----------------------------
# SMS FUNCTION
# -----------------------------
def send_sms(message):
    st.toast("📱 SMS Alert Sent!")
    st.warning(message)

# -----------------------------
# FORECAST LOGIC
# -----------------------------
if run_button:

    with st.spinner("Running AI Simulation..."):
        time.sleep(1)

        base_storage = storage * 100
        forecast_data = []

        for day in range(1, 16):

            change = random.uniform(-3, 6)
            base_storage += change
            probability = random.randint(10, 95)

            if probability > 80:
                risk = "Severe Flood Risk"
            elif probability > 60:
                risk = "Flood Risk"
            elif probability < 30:
                risk = "Water Scarcity Risk"
            else:
                risk = "Safe"

            forecast_data.append({
                "Day": day,
                "Predicted Storage": round(base_storage, 2),
                "Flood Probability (%)": probability,
                "Risk Status": risk
            })

        df = pd.DataFrame(forecast_data)

    # -----------------------------
    # KPI SECTION
    # -----------------------------
    st.markdown("---")
    st.subheader("📊 Forecast Summary")

    colA, colB, colC = st.columns(3)

    final_storage = df.iloc[-1]["Predicted Storage"]
    final_prob = df.iloc[-1]["Flood Probability (%)"]
    final_risk = df.iloc[-1]["Risk Status"]

    colA.metric("Final Storage", final_storage)
    colB.metric("Flood Probability", f"{final_prob}%")
    colC.metric("Risk Status", final_risk)

    # -----------------------------
    # GRAPH
    # -----------------------------
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
        height=450,
        xaxis_title="Day",
        yaxis_title="Storage Level"
    )

    st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # TABLE
    # -----------------------------
    st.subheader("📋 15-Day Forecast Table")
    st.dataframe(df, use_container_width=True)

    # -----------------------------
    # ALERT TRIGGER
    # -----------------------------
    if "Severe" in final_risk:
        send_sms(f"🚨 Severe Flood Risk at {selected_reservoir}")
    elif "Flood" in final_risk:
        send_sms(f"⚠ Flood Warning at {selected_reservoir}")