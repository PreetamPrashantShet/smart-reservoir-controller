National Water Intelligence System

AI-Powered Reservoir Forecasting & Flood Risk Monitoring Platform

🏛 Overview

The National Water Intelligence System (NWIS) is an AI-driven decision-support platform designed to assist government authorities in:

Reservoir level forecasting (15-Day Prediction)

Flood risk detection & probability scoring

Geospatial river basin intelligence mapping

Automated alert escalation simulation

State-wise reservoir analytics

Role-based secure dashboard access

This system demonstrates how machine learning, geospatial analytics, and intelligent monitoring can improve disaster preparedness and water resource optimization.

🚀 Key Features

📊 1. 15-Day AI Reservoir Forecast

Predicts storage levels for 15 days

Flood probability estimation

Risk classification:

🔴 Critical Flood Risk (≥ 90%)

🟠 Flood Warning (≥ 50%)

🟡 Normal Monitoring (< 50%)

Interactive Plotly visualization

Color-coded analytics table

🗺 2. Geospatial Risk Monitoring

Multi-river basin intelligence

India-focused geo visualization

Basin-level risk overview

🧠 System Architecture

National KPI dashboard (Severe / Warning / Safe)

🚨 3. Automated Alert System

Risk-based SMS simulation

Alert escalation logic

Real-time visual alerts

Role-aware notification control

🔐 4. Secure Government Login System

Role-based authentication:

Admin

Authority

Viewer

Password hashing (SHA-256)

Session-based access protection

Dashboard access control

🏞 5. State-Wise Reservoir Analysis

Reservoir selection per state

Dynamic risk simulation

Custom parameter inputs

Real-time predictive analytics

🧠 System Architecture

User Input
    ↓
Streamlit Frontend (UI)
    ↓
FastAPI Backend
    ↓
Forecast Logic / ML Simulation
    ↓
Risk Classification Engine
    ↓
Visualization + Alert System

🛠 Technology Stack

| Layer            | Technology                 |
| ---------------- | -------------------------- |
| Frontend         | Streamlit                  |
| Backend          | FastAPI                    |
| Visualization    | Plotly                     |
| Data Handling    | Pandas                     |
| Auth System      | Session-based Role Control |
| Deployment Ready | Python 3.10+               |

⚙ Installation & Setup

1️⃣ Clone Repository

git clone https://github.com/yourusername/national-water-intelligence-system.git

cd national-water-intelligence-system

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run Backend (FastAPI)

python -m uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000

4️⃣ Run Frontend (Streamlit)

python -m streamlit run login.py

📊 Risk Classification Logic

if probability >= 90:
    risk = "Critical Flood Risk"
elif probability >= 50:
    risk = "Flood Warning"
else:
    risk = "Normal Monitoring"
    
🎯 Use Cases

Disaster Management Authority Monitoring

Reservoir Management Optimization

Flood Early Warning Systems

State-Level Water Governance

Academic & Research Demonstration

🔮 Future Enhancements

Real-time IMD rainfall API integration

Historical dataset ML training

SMS integration (Twilio)

PostgreSQL production database

Role-based audit logs

Cloud deployment (AWS / Azure)

CI/CD pipeline integration

PDF report export system

📈 Why This Project Matters

Water resource mismanagement and delayed flood warnings result in severe socio-economic damage.

This system demonstrates how:

AI-based forecasting

Risk scoring

Geospatial mapping

Alert automation

can support national-scale decision-making.

👨‍💻 Author

Preetam P Shet

AI & Data Systems Developer

India

📜 License

This project is for academic and demonstration purposes.

⭐ If you like this project, give it a star on GitHub!

