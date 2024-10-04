from joblib import load
import pandas as pd
import numpy as np
import streamlit as st
import psycopg2
from datetime import datetime

db_params = {
    "host": "localhost",
    "database": "AgriKnow",
    "user": "postgres",
    "password": "admin123"
}

def connect_to_db():
    return psycopg2.connect(**db_params)

def insert_users_data(number, result):
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute(
    "INSERT INTO model1_data (number, model1_result) VALUES (%s, %s)",
    (number, result)
    )
    conn.commit()
    cur.close()
    conn.close()

st.logo(r"C:\Users\tharu\OneDrive\Pictures\Screenshots 1\Screenshot 2024-07-13 144102.png")
st.set_page_config(layout="wide")
model_premium = load("svr_premium_model.joblib")
input_sc = load("sc_input_premium")
output_sc = load("sc_output_premium")


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
    user_number = st.session_state.get('user_number')
    formatted_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    insert_users_data(user_number, str(y[0][0]))
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
    if selected is not None:
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    

st.button("predict", on_click=predict)
col = st.columns

    
    