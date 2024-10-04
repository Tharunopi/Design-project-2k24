import streamlit as st
import psycopg2
import psycopg2.extras
from psycopg2.extras import Json
import pandas as pd
import hashlib, time

st.logo(r"C:\Users\tharu\OneDrive\Pictures\Screenshots 1\Screenshot 2024-07-13 144102.png")
st.set_page_config(layout="wide")

db_params = {
    "host": "localhost",
    "database": "AgriKnow",
    "user": "postgres",
    "password": "admin123"
}

def connect_to_db():
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    return conn
    
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_number(x):
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute('SELECT number FROM users')
    results = cur.fetchall()

    cur.close()
    conn.close()

    number = [i[0] for i in results]
    if x not in number:
        return True
    else:
        return False

def area_planted(x):
    data = []
    for i in range(1, int(x)+1):
        crop = st.text_input(f"Enter crop {i}", key=f"crop_{i}")
        area = st.select_slider(
            f"Select acre of {i} crop",
            [i for i in range(1, 11)],
            value=1,
            key=f"crop_{i}_1"
        )
        data.append([crop, area])
    return {'data': data}
    
def insert_user(number, name, location, password, land_area, planted, email):
    conn = connect_to_db()
    cur = conn.cursor()
    hashed_password = hash_password(password)
    cur.execute(
        "INSERT INTO users (number, name, location, password, land_area, planted, email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (number, name, location, hashed_password, land_area, planted, email)
    )
    conn.commit()
    cur.close()
    conn.close()
    
st.header("Signup")
new_name = st.text_input("Name")
new_number = st.text_input("Number")
new_location = st.text_input("Location(District)")
new_password = st.text_input("Password", type="password")
new_land_area = st.number_input("Land Area")
new_varietycrop_plantes = st.selectbox("How many variety of crops planted in your field?", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], placeholder="Choose any variety")
value = area_planted(new_varietycrop_plantes)
st.write(new_varietycrop_plantes)
planted_json = Json(value)
new_planted = planted_json
new_email = st.text_input("Email(Optional)")
col11, col12, col13, col14, col15, col16, col17 = st.columns(7)
with col14:
    if st.button("Sign up"):
        if len(new_number) != 10:
            st.error("Enter a valid mobile number")
        elif not check_number(new_number):
            st.error(f"Number {new_number} already exists!")
        elif not new_name or not new_location or not new_password:
            st.error("Please fill in all required fields")
        else:    
            insert_user(new_number, new_name, new_location, new_password, new_land_area, new_planted, new_email)
            st.success("Proceed to login")