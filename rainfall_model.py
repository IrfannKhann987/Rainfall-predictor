import pickle
import streamlit as st
import numpy as np
#***********************************MODEL**************************************
with open("random_forest_model.pkl", "rb") as f:
    rf_model = pickle.load(f)


st.title("Rainfall Predictor app")
st.markdown("Enter weather conditions below and predict if it will rain or not!")
#_______________________________INPUT_VALUES______________________________________

pressure = st.number_input("Pressure (hPa)", value=1010.0)
dewpoint = st.number_input("Dew Point (°C)", value=22.0)
humidity = st.number_input("Humidity (%)", value=85.0)
cloud = st.number_input("Cloud (oktas)", value=6.0)
sunshine = st.number_input("Sunshine (hours)", value=3.0)
winddirection = st.number_input("Wind Direction (°)", value=180.0)
windspeed = st.number_input("Wind Speed (km/h)", value=12.0)

# Collect input into numpy array
features = np.array([[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]])

if st.button("Predict"):
    prediction = rf_model.predict(features)[0]
    st.success("🌧️ Rain is likely!" if prediction == 1 else "☀️ No rain expected.")

