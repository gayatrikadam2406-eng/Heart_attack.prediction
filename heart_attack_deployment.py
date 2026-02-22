# Heart Attack Prediction App

import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("dtc_model(1).pkl")

st.title("Heart_attack_prediction")

# Inputs
Age = st.number_input("Age")
Gender = st.selectbox("Gender (0 = Female, 1 = Male)", [0, 1])
Heart_rate = st.number_input("Heart rate")
Systolic_bp = st.number_input("Systolic blood pressure")
Diastolic_bp = st.number_input("Diastolic blood pressure")
Blood_sugar = st.number_input("Blood sugar")
CK_MB = st.number_input("CK-MB")
Troponin = st.number_input("Troponin")

# IMPORTANT: Column names MUST match training dataset EXACTLY
input_data = pd.DataFrame([[
    Age,
    Gender,
    Heart_rate,
    Systolic_bp,
    Diastolic_bp,
    Blood_sugar,
    CK_MB,
    Troponin
]], columns=[
    "Age",
    "Gender",
    "Heart rate",
    "Systolic blood pressure",
    "Diastolic blood pressure",
    "Blood sugar",
    "CK-MB",
    "Troponin"
])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.success("The patient is Normal")
    else:
        st.error("The patient has Heart Disease")
