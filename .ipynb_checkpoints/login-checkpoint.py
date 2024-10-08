import streamlit as st
import psycopg2
import hashlib
import time

st.logo(r"C:\Users\tharu\OneDrive\Pictures\Screenshots 1\Screenshot 2024-07-13 144102.png")
db_params = {
    "host": "localhost",
    "database": "AgriKnow",
    "user": "postgres",
    "password": "admin123"
}

def connect_to_db():
    return psycopg2.connect(**db_params)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_user_login(number, password):
    conn = connect_to_db()
    cur = conn.cursor()
    hashed_password = hash_password(password)
    cur.execute("SELECT * FROM users WHERE number = %s AND password = %s", (number, hashed_password))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    col1, col2, col3, col4, col5 = st.columns(5)
    col3.header("Login")

    login_number = st.text_input("Number")
    login_password = st.text_input("Password", type="password")
    
    col11, col12, col13, col14, col15 = st.columns(5)
    with col13:
        if st.button("Login"):
            user = check_user_login(login_number, login_password)
            if user:
                st.session_state['logged_in'] = True
                st.session_state['user_number'] = login_number  
                st.success("Login successful!")
                with st.spinner("Logging in..."):
                    time.sleep(3)
                
                st.rerun()  
            else:
                st.error("Invalid credentials")
else:
    home_page = st.Page("first.py", title="Home")
    cnn_page = st.Page("AAcnn_model.py", title="CNN")
    chatbot = st.Page("Chatbot.py", title="Chatbot")
    model = st.Page("model.py", title="Model-1")
    model2 = st.Page("model2.py", title="Model-2")
    tech = st.Page("Data_alteration.py", title="Datasets")
    profile = st.Page("profile.py", title="Profile")

    pg = st.navigation([home_page, cnn_page, chatbot, model, model2, tech, profile])
    pg.run()
