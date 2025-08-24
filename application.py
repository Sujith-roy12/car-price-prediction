import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open("LinearReg.pkl", "rb"))

st.title("🚗 Car Price Prediction App")

st.write("Enter the car details below to predict its selling price.")

# Input fields
name = st.text_input("Car Name (e.g., Maruti Suzuki Swift)")
company = st.text_input("Company (e.g., Maruti)")
year = st.number_input("Year of Purchase", min_value=1990, max_value=2025, step=1)
kms_driven = st.number_input("Kilometers Driven", min_value=0, step=1000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])

# Predict button
if st.button("Predict Price"):
    # ✅ Pass input as DataFrame with the same column names used during training
    input_df = pd.DataFrame([[name, company, year, kms_driven, fuel_type]],
                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Price: ₹ {int(prediction)}")
