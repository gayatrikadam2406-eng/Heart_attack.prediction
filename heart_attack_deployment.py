# Heart Attack Prediction App

import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load trained model
model = joblib.load("dtc_model(1).pkl")

st.title("Heart Attack Prediction")

# User Inputs
Age = st.number_input("Age")
Gender = st.number_input("Gender (0 = Female, 1 = Male)")
Heart_rate = st.number_input("Heart Rate")
Systolic_blood_pressure = st.number_input("Systolic Blood Pressure")
Diastolic_blood_pressure = st.number_input("Diastolic Blood Pressure")
Blood_sugar = st.number_input("Blood Sugar")
CK_MB = st.number_input("CK-MB")
Troponin = st.number_input("Troponin")

# Create DataFrame (ONLY FEATURES — no Result column)
input_data = pd.DataFrame([{
    "Age": Age,
    "Gender": Gender,
    "Heart rate": Heart_rate,
    "Systolic blood pressure": Systolic_blood_pressure,
    "Diastolic blood pressure": Diastolic_blood_pressure,
    "Blood sugar": Blood_sugar,
    "CK-MB": CK_MB,
    "Troponin": Troponin
}])

# Prediction Button
if st.button("Predict"):

    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.success("The patient is Normal")
    else:
        st.error("The patient has Heart Disease")
