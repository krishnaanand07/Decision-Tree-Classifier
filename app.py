import streamlit as st
import pandas as pd
import joblib

model = joblib.load("decision_tree_model.joblib")

st.title("Credit Card Fraud Detection")

time = st.number_input("Enter Time")
amount = st.number_input("Enter Amount")

if st.button("Predict"):

    input_data = [[time, amount]]

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Fraud Transaction")
    else:
        st.success("Legitimate Transaction")