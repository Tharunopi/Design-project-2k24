import streamlit as st
import psycopg2

db_params = {
    "host": "localhost",
    "database": "AgriKnow",
    "user": "postgres",
    "password": "admin123"
}

def connect_to_db():
    return psycopg2.connect(**db_params)

def get_user_data(number):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE number = %s", (number,))
    user_data = cur.fetchone()
    cur.close()
    conn.close()
    return user_data

if 'logged_in' in st.session_state and st.session_state['logged_in']:
    user_number = st.session_state.get('user_number')  

    user_data = get_user_data(user_number)

    if user_data:
        st.header("Profile Page")
        st.write(f"**Name:** {user_data[1]}")  
        st.write(f"**Number:** {user_data[0]}")  
        st.write(f"**Location:** {user_data[2]}")  
        st.write(f"**Land Area:** {user_data[4]}")  
        st.write(f"**Planted:** {user_data[5]}")  
        st.write(f"**Email:** {user_data[6]}")  
    else:
        st.error("User data not found.")
else:
    st.error("You need to log in to view this page.")
