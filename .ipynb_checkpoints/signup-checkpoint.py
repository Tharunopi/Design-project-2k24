import streamlit as st
import psycopg2
import pandas as pd
import hashlib

db_params = {
    "host": "localhost",
    "database": "AgriKnow",
    "user": "postgres",
    "password": "admin123"
}

def connect_to_db():
    conn = psycopg2.connect(**db_params)
    return conn
    
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
    
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
new_planted = st.text_input("Planted (as JSON)")
new_email = st.text_input("Email(Optional)")
col11, col12, col13, col14, col15, col16, col17 = st.columns(7)
with col14:
    if st.button("Sign up"):
        insert_user(new_number, new_name, new_location, new_password, new_land_area, new_planted, new_email)
        st.success("Proceed to login")