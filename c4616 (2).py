# -*- coding: utf-8 -*-
"""c4616.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ENJcutUdGH_ukqVMBswyO042J3XMo0mh
"""

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# App Title
st.title("🚗 Car Evaluation Classifier using Random Forest & Streamlit")
st.write("Predict the car condition using Machine Learning based on various features.")
st.markdown(" *Made by: Vishal*")

# File uploader
uploaded_file = st.file_uploader("📁 Upload your car.csv file", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Dataset Preview")
    st.dataframe(df.head())

    # Encoding categorical columns if needed
    df_encoded = df.apply(lambda col: pd.factorize(col)[0])

    # Splitting data
    X = df_encoded.iloc[:, :-1]
    y = df_encoded.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Accuracy
    accuracy = model.score(X_test, y_test)
    st.success(f"🎯 Model Accuracy: {accuracy*100:.2f}%")

    # Prediction UI
    st.subheader("🧪 Predict Car Condition")

    input_data = []
    for column in df.columns[:-1]:
        value = st.selectbox(f"{column}", df[column].unique())
        input_data.append(value)

    # Convert input to encoded form
    input_encoded = [pd.Series(df[column].unique()).tolist().index(val) for column, val in zip(df.columns[:-1], input_data)]
    prediction = model.predict([input_encoded])[0]

    # Decode prediction
    decoded_label = pd.Series(df[df.columns[-1]].unique())[prediction]
    st.success(f"✅ Predicted Condition: {decoded_label}")

    st.markdown("❤ **Made with love by Vshal **")
else:
    st.warning("⚠ Please upload the car.csv file to proceed.")