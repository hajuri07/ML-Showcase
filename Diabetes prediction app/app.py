# app.py
import streamlit as st
import numpy as np
import joblib

# Load your combined scaler + model bundle
bundle = joblib.load("scaler_model_bundle.joblib")
scaler = bundle["scaler"]
model = bundle["model"]

st.set_page_config(page_title="🩺 Diabetes Prediction App", layout="centered")

st.title("🩺 Diabetes Prediction App")
st.markdown("### Enter your health details below to predict diabetes:")

# User input fields
Pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=1)
Glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
BloodPressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=200, value=70)
SkinThickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
Insulin = st.number_input("Insulin (µU/ml)", min_value=0, max_value=900, value=80)
BMI = st.number_input("BMI", min_value=0.0, max_value=70.0, value=28.0)
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
Age = st.number_input("Age", min_value=0, max_value=120, value=33)

# When Predict button is clicked
if st.button("🔮 Predict"):
    # Prepare input data in same order used for training
    user_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, 
                           Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    # Scale input and make prediction
    user_scaled = scaler.transform(user_data)
    prediction = model.predict(user_scaled)[0]
    probability = model.predict_proba(user_scaled)[0][1]

    # Display results
    st.subheader("Prediction Result:")
    if prediction == 1:
        st.error(f"⚠️ Model predicts: **Diabetic** (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Model predicts: **Non-Diabetic** (Probability: {probability:.2f})")
