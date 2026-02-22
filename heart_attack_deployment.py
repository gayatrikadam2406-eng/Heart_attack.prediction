# Heart Attack Prediction App

import streamlit as st
import joblib

model = joblib.load("dtc_model(1) (1).pkl")

st.title("Heart_attack_prediction !")

Age = st.number_input("Age")
Gender = st.number_input("Gender")
Heart_rate = st.number_input("Heart_rate")
Systolic_blood_pressure = st.number_input("Systolic_blood_pressure")
Diastolic_blood_pressure = st.number_input("Diastolic_blood_pressure")
Blood_sugar = st.number_input("Blood_sugar")
CK-MB = st.number_input("CK-MB")
Troponin = st.number_input("Troponin")
Result = st.number_input("Result")


input_data = pd.DataFrame({
    "Age": Age,
    "Gender": Gender,
    "Heart_rate": Heart_rate,
    "Systolic_blood_pressure": Systolic_blood_pressure,
    "Diastolic_blood_pressure": Diastolic_blood_pressure,
    "Blood_sugar": Blood_sugar,
    "CK-MB": CK-MB,
    "Troponin": Troponin,
    "Result": Result
    
})

if st.button("Predict"):

    input_array = np.array([input_data])

    prediction = model.predict(input_array)[0]

    if prediction == 0:
        st.write("The patient is Normal")
    else:
        st.write("The patient has Heart Disease")
