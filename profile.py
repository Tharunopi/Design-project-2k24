import streamlit as st
import psycopg2
import time
import pandas as pd

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

def fetch_db_id():
    conn = connect_to_db()
    cur = conn.cursor()
    
    cur.execute("SELECT id FROM users")
    results = cur.fetchall()
    
    cur.close()
    conn.close()

    return [i[0] for i in results]

def fetch_db_planted():
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE number = %s", (number,))
    results = cur.fetchone()

    cur.close()
    conn.close()

    return results

def data_filter(x):
    li = x["data"]
    return li
    
if 'logged_in' in st.session_state and st.session_state['logged_in']:
    user_number = st.session_state.get('user_number')  

    user_data = get_user_data(user_number)
    if user_data:
        st.header("Profile")
        st.divider()
        st.subheader("User Info")
        u_id, name, number, location, land_area, planted, email = user_data[0], user_data[2], user_data[1], user_data[3], user_data[5], user_data[6], user_data[7]
        data_after_filter = data_filter(fetch_db_planted()[6])
        col1, col2, col3 = st.columns(3)
        col1.write(f"**Name:** {name}")  
        col1.write(f"**Number:** {number}")  
        col2.write(f"**Location:** {location}")  
        col2.write(f"**Land Area:** {land_area} acre")  
        col3.write(f"**Total area planted:** {sum([i[1] for i in data_after_filter])}")  
        if email:
            col3.write(f"**Email:** {email}") 

        st.divider()
        st.subheader("Dashboard")
        col11, col12, col13, col14, col15 = st.columns(5)
        col13.markdown("Area Analysis")
        chart_data = pd.DataFrame({
            'crops': [i[0] for i in data_after_filter],
            'area': [i[1] for i in data_after_filter] 
        })
        st.bar_chart(chart_data,x='area', y='crops',x_label="Acres", y_label = "Crops", color='area', height=500, width=100)
        st.divider()

        st.subheader(f"What AgriKnow tells about {location}'s Geographical Information")
        col21, col22, col23 = st.columns(3)
        col22.markdown("Coming Soon...")
        st.divider()

        st.subheader(f"Get personalized suggestion from AgriKnow")
        col31, col32, col33 = st.columns(3)
        col32.markdown("Coming Soon...")
        st.divider()

        st.subheader(f"Fertilizer suggested by AgriKnow for your planted crops")
        col41, col42, col43 = st.columns(3)
        col42.markdown("Coming Soon...")
        st.divider()

        st.caption(f'Total accounts created {fetch_db_id()[-1]}')

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
