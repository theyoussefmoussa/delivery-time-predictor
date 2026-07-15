import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
BASE_PATH = os.getenv("BASE_PATH")

st.set_page_config(
    page_title="Delivery Time Predictor",
    page_icon="📦",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: #f7f8fa;
}

h1, h2, h3, p, label, .stMarkdown {
    color: #1c2530 !important;
    font-family: 'Helvetica Neue', Arial, sans-serif;
}

.header {
    padding: 1.2rem 0 0.4rem 0;
    border-bottom: 1px solid #e2e5e9;
    margin-bottom: 1.8rem;
}
.header h1 {
    font-size: 1.6rem;
    font-weight: 600;
    margin: 0;
}
.header p {
    color: #5b6472 !important;
    font-size: 0.95rem;
    margin-top: 0.3rem;
}

section[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e2e5e9;
}
section[data-testid="stSidebar"] h3 {
    font-size: 0.95rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: #5b6472 !important;
}

.stButton > button {
    background: #0d6f66;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 0.6rem 1.2rem;
    font-weight: 500;
    font-size: 0.95rem;
    width: 100%;
}
.stButton > button:hover {
    background: #0a5951;
    color: white;
    border: none;
}

.result-box {
    background: white;
    border: 1px solid #e2e5e9;
    border-left: 4px solid #0d6f66;
    border-radius: 6px;
    padding: 1.6rem 1.8rem;
    margin-top: 1.5rem;
}
.result-box .sentence {
    font-size: 1.15rem;
    line-height: 1.6;
    margin: 0;
}
.result-box .sentence strong {
    color: #0d6f66;
}
.result-box .sub {
    color: #5b6472 !important;
    font-size: 0.88rem;
    margin-top: 0.6rem;
}

.stNumberInput, .stSelectbox {
    margin-bottom: 0.4rem;
}
</style>
""", unsafe_allow_html=True)

model = joblib.load(f"{BASE_PATH}/models/linear_regression.pkl")
scaler = joblib.load(f"{BASE_PATH}/models/scaler.pkl")

FEATURE_COLUMNS = [
    'Distance_m', 'Traffic_Level', 'Preparation_Time_min', 'Courier_Experience_yrs',
    'Weather_Foggy', 'Weather_Rainy', 'Weather_Snowy', 'Weather_Windy',
    'Time_of_Day_Evening', 'Time_of_Day_Morning', 'Time_of_Day_Night',
    'Vehicle_Type_Car', 'Vehicle_Type_Scooter'
]

NUMERIC_COLUMNS = ['Distance_m', 'Preparation_Time_min', 'Courier_Experience_yrs']

TRAFFIC_MAP = {"Low": 0, "Medium": 1, "High": 2}

st.markdown("""
<div class="header">
    <h1>Delivery Time Predictor</h1>
    <p>Estimate arrival time from distance, weather, traffic and courier experience.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Trip Details")
    distance = st.number_input("Distance (meters)", min_value=0, max_value=25000, value=5000, step=100)
    prep_time = st.number_input("Preparation Time (minutes)", min_value=0, max_value=60, value=15)
    experience = st.number_input("Courier Experience (years)", min_value=0, max_value=20, value=2)

    st.markdown("### Conditions")
    traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
    weather = st.selectbox("Weather", ["Clear", "Foggy", "Rainy", "Snowy", "Windy"])
    time_of_day = st.selectbox("Time of Day", ["Afternoon", "Evening", "Morning", "Night"])
    vehicle = st.selectbox("Vehicle Type", ["Bike", "Car", "Scooter"])

    predict_clicked = st.button("Guess when the order arrives")

if predict_clicked:
    row = {col: 0 for col in FEATURE_COLUMNS}

    row['Distance_m'] = distance
    row['Preparation_Time_min'] = prep_time
    row['Courier_Experience_yrs'] = experience
    row['Traffic_Level'] = TRAFFIC_MAP[traffic]

    if weather != "Clear":
        row[f"Weather_{weather}"] = 1

    if time_of_day != "Afternoon":
        row[f"Time_of_Day_{time_of_day}"] = 1

    if vehicle != "Bike":
        row[f"Vehicle_Type_{vehicle}"] = 1

    input_df = pd.DataFrame([row])[FEATURE_COLUMNS]
    input_df[NUMERIC_COLUMNS] = scaler.transform(input_df[NUMERIC_COLUMNS])

    prediction = model.predict(input_df)[0]
    arrival_clock = (datetime.now() + timedelta(minutes=prediction)).strftime("%I:%M %p")

    st.markdown(f"""
    <div class="result-box">
        <p class="sentence">Based on current conditions, the order should arrive in about <strong>{prediction:.0f} minutes</strong> — around <strong>{arrival_clock}</strong>.</p>
        <p class="sub">{distance:,} m · {traffic} traffic · {weather} · {time_of_day} · {vehicle}</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="result-box">
        <p class="sentence" style="color:#5b6472;">Fill in the trip details on the left and click <strong>Guess when the order arrives</strong>.</p>
    </div>
    """, unsafe_allow_html=True)