# Heart Attack Prediction App

import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("dtc_model(1).pkl")

st.title("Heart_attack_prediction")

st.write("Enter patient medical details below:")

# User Inputs
Age = st.number_input("Age", min_value=0)
Gender = st.selectbox("Gender", [0, 1])  # 0 = Female, 1 = Male
Heart_rate = st.number_input("Heart Rate", min_value=0)
Systolic_blood_pressure = st.number_input("Systolic Blood Pressure", min_value=0)
Diastolic_blood_pressure = st.number_input("Diastolic Blood Pressure", min_value=0)
Blood_sugar = st.number_input("Blood Sugar", min_value=0.0)
CK_MB = st.number_input("CK-MB", min_value=0.0)
Troponin = st.number_input("Troponin", min_value=0.0)

# Create input dataframe (must match training column names exactly)
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
