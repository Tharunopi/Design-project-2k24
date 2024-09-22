import streamlit as st
import psycopg2
import hashlib

# Database parameters
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

# Check if the user is logged in
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.header("Login")

    login_number = st.text_input("Number")
    login_password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = check_user_login(login_number, login_password)
        if user:
            st.session_state['logged_in'] = True
            st.session_state['user_number'] = login_number  # Store the user number
            st.success("Login successful!")
            # st.experimental_rerun()  # Optionally refresh to redirect
        else:
            st.error("Invalid credentials")
else:
    # Navigation for logged-in users
    home_page = st.Page("first.py", title="Home")
    cnn_page = st.Page("AAcnn_model.py", title="CNN")
    chatbot = st.Page("Chatbot.py", title="Chatbot")
    model = st.Page("model.py", title="Model-1")
    model2 = st.Page("model2.py", title="Model-2")
    tech = st.Page("Data_alteration.py", title="Datasets")
    profile = st.Page("profile.py", title="Profile")

    pg = st.navigation([home_page, cnn_page, chatbot, model, model2, tech, profile])
    # st.set_page_config(page_title="Data manager", page_icon=":material/edit:", layout="wide")
    pg.run()
