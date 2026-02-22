# Heart Attack Prediction App

import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("dtc_model(1).pkl")

st.title("Heart Attack Prediction")

# Show expected model features (for debugging - you can remove later)
st.write("Model expects:", model.feature_names_in_)

# User Inputs
Age = st.number_input("Age")
Gender = st.number_input("Gender (0 = Female, 1 = Male)")
Heart_rate = st.number_input("Heart Rate")
Systolic_blood_pressure = st.number_input("Systolic Blood Pressure")
Diastolic_blood_pressure = st.number_input("Diastolic Blood Pressure")
Blood_sugar = st.number_input("Blood Sugar")
CK_MB = st.number_input("CK-MB")
Troponin = st.number_input("Troponin")

if st.button("Predict"):

    # Store input values in same order as model expects
    values = [
        Age,
        Gender,
        Heart_rate,
        Systolic_blood_pressure,
        Diastolic_blood_pressure,
        Blood_sugar,
        CK_MB,
        Troponin
    ]

    # Create DataFrame using model's exact feature names
    input_data = pd.DataFrame([values], columns=model.feature_names_in_)

    # Make prediction
    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.success("The patient is Normal")
    else:
        st.error("The patient has Heart Disease")
