from joblib import load
import pandas as pd
import numpy as np
import streamlit as st

model_premium = load("svr_premium_model.joblib")
input_sc = load("sc_input_premium")
output_sc = load("sc_output_premium")
# prediction_data = input_sc.transform([[1230.0, 80.0, 28, 80.0, 24.0, 20.0]])
# output_sc.inverse_transform([(model_premium.predict(prediction_data))])


st.title("premium model 😮‍💨")
rain = st.text_input("Rainfall", "1230")
fertilizer = st.text_input("Fertilizer", "80")
temp = st.slider("temperature", 10, 80)
nitrogen = st.text_input("nitrogen", "80")
phos = st.text_input("phosporus", "24")
potasium = st.text_input("potasium", "20")

def predict():
    x = input_sc.transform([[rain, fertilizer, temp, nitrogen, phos, potasium]])
    result = model_premium.predict(x)
    y = output_sc.inverse_transform([result])
    st.success(f"Expected yield Q/Acre is {y[0][0]}")
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
    if selected is not None:
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    

st.button("predict", on_click=predict)
col = st.columns

    
    