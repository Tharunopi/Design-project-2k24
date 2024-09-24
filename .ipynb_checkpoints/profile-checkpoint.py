import streamlit as st
import psycopg2
import time

st.logo(r"C:\Users\tharu\OneDrive\Pictures\Screenshots 1\Screenshot 2024-07-13 144102.png")
st.set_page_config(layout="wide")
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
        st.header("Profile")
        st.divider()
        st.subheader("User Info")
        u_id, name, number, location, land_area, planted, email = user_data[0], user_data[2], user_data[1], user_data[3], user_data[5], user_data[6], user_data[7]
        col1, col2, col3 = st.columns(3)
        col1.write(f"**Name:** {name}")  
        col1.write(f"**Number:** {number}")  
        col2.write(f"**Location:** {location}")  
        col2.write(f"**Land Area:** {land_area}")  
        col3.write(f"**Planted:** {planted}")  
        if email:
            col3.write(f"**Email:** {email}") 

        col2.caption(f'Total accounts created {u_id}')

        st.subheader("Dashboard")
        st.markdown("Area Analysis")

        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.session_state.pop('user_number', None) 
            st.success("You have been logged out.")
            with st.spinner("Logging out..."):
                time.sleep(3)
            st.rerun()
    else:
        st.error("User data not found.")
else:
    st.error("You need to log in to view this page.")
