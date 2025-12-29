# Save this as app.py or run in a notebook cell with `streamlit` magic
import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# 1. Load trained model
# -------------------------------
with open('linear_model.pkl', 'rb') as f:
    model = pickle.load(f)

# -------------------------------
# 2. Streamlit Frontend
# -------------------------------
st.title("NASA Airfoil Sound Pressure Prediction")

st.write("Enter the values for each feature:")

# User inputs
frequency = st.number_input("Frequency (Hz)", value=1000, step=1)
angle = st.number_input("Angle of Attack (degrees)", value=5.0, step=0.1)
gaudlance = st.number_input("Gaudlance", value=0.5, step=0.01)
speed = st.number_input("Speed of Air (m/s)", value=50.0, step=0.1)
displacement = st.number_input("Displacement", value=0.01, step=0.001)

# Predict button
if st.button("Predict Sound Pressure"):
    X_new = pd.DataFrame([[frequency, angle, gaudlance, speed, displacement]],
                         columns=['Frequency','Angle','Chord Length','Speed of Air','Displacement'])
    prediction = model.predict(X_new)
    st.success(f"Predicted Sound Pressure: {prediction[0]:.2f}")
