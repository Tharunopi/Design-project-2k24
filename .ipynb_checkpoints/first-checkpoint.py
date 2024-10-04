import streamlit as st
import pandas as pd
import time, random
import psycopg2
import requests
from joblib import load
import folium
from streamlit_folium import st_folium
from streamlit_extras.mention import mention
st.logo(r"C:\Users\tharu\OneDrive\Pictures\Screenshots 1\Screenshot 2024-07-13 144102.png")
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

def insert_users_data(number, result):
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute(
    "INSERT INTO weather_data (number, weather_result) VALUES (%s, %s)",
    (number, result)
    )
    conn.commit()
    cur.close()
    conn.close()

if 'logged_in' in st.session_state and st.session_state['logged_in']:
    user_number = st.session_state.get('user_number')  
    user_data = get_user_data(user_number)

name, number, location, land_area, planted, email = user_data[2], user_data[1], user_data[3], user_data[5], user_data[6], user_data[7]

API_KEY = 'ba2e7ef8a27142ddb2b43315242009'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

def get_weather(city_name):
    params = {
        'key': API_KEY,
        'q': city_name,
        'aqi': 'no'  
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return f"Error: {response.status_code}"

weather_info = get_weather(location)

def weather():
    pred = [[weather_info["current"]["pressure_mb"], weather_info["current"]["temp_c"], weather_info["current"]["dewpoint_c"], weather_info["current"]["humidity"], weather_info["current"]["cloud"], weather_info["current"]["wind_kph"], weather_info["current"]["wind_degree"]]]

    weather_model = load(r'weather_model')
    sc_weather = load(r'sc_weather_model')

    pred = sc_weather.transform(pred)
    r = weather_model.predict(pred)
    rainfall = ""
    if r == 0:
        rainfall += "No🌥️"
    else:
        rainfall += "Yes🌦️"
        
    user_number = st.session_state.get('user_number')
    insert_users_data(user_number, rainfall)
    return rainfall

st.title(f"Hi {name}, Welcome to AgriKnow")
st.divider()

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Temperature🌞", str(weather_info["current"]["temp_c"])+"°C")
col1.caption(f'Feels like {str(weather_info["current"]["feelslike_c"]) + "°C"}')

col2.metric("Wind🌬️", str(weather_info["current"]["wind_kph"])+"Kph")
col2.caption(f'Location {location}')

col3.metric("Humidity💦", str(weather_info["current"]["humidity"])+"%")
col3.caption(f'Cloud {str(weather_info["current"]["cloud"])}%')

col4.metric("Rainfall prediction",weather())
col4.caption("This does not resembles 100% accurate data")

col5.markdown(f'Last updated: {weather_info["current"]["last_updated"]}')

tab1, tab2, tab3 = st.tabs(["Overview", "Technology", "Key features"])

with tab1:
    st.subheader("Overview")
    st.markdown("By leveraging machine learning (ML) models, a Convolutional Neural Network (CNN), and a chatbot interface, farmers can receive real-time insights and recommendations tailored to their specific farming needs.")
    coll1, coll2, coll3 = st.columns(3)
    coll2.image(r"ai wheat.jpg", width=400)
    coll2.caption("Image represents Overview of the project")

with tab2:
    st.subheader("Technologies Used")
    st.markdown("Machine Learning: Random Forest, Gradient Boosting")
    st.markdown("Deep Learning: CNN (MobileNet)")
    st.markdown("Chatbot Integration: Gemini API")
    st.markdown("Future Integration: YOLO (object detection), Sign-based LLM")
    collu1, collu2, collu3 = st.columns(3)
    collu2.image(r"ai wheat2.jpg", width=500)
    collu2.caption("Image represents Technology that are used in this project")

with tab3:
    st.subheader("Key features")
    st.markdown("Yield Prediction")
    st.markdown("Disease Detection")
    st.markdown("Farmer Chatbot")

data = {
    'District': ['Amritsar', 'Ludhiana', 'Patiala', 'Karnal', 'Hisar', 'Ambala', 'Bareilly', 'Lucknow', 'Kanpur', 
                 'Indore', 'Guna', 'Mandsaur', 'Sri Ganganagar', 'Hanumangarh', 'Purnia', 'Saran', 'Sabarkantha'],
    'Latitude': [31.6340, 30.9009, 43.0074, 29.6838, 29.1394, 30.3782, 28.3670, 26.8467, 26.4499, 
                 22.7196, 24.6868, 24.0932, 29.9258, 29.1760, 25.7670, 25.9060, 23.4300],
    'Longitude': [74.8723, 75.8573, 76.5216, 76.9808, 75.5734, 76.7790, 79.4304, 80.9462, 80.3240, 
                  75.8573, 77.2404, 75.8892, 73.2614, 75.7580, 85.0607, 84.1145, 72.8977],
    'Wheat_Production': [100000, 150000, 200000, 120000, 130000, 140000, 110000, 160000, 170000, 
                         180000, 190000, 150000, 140000, 130000, 120000, 110000, 100000]
}

df = pd.DataFrame(data)

st.title('Major Wheat Producing Districts in India')

st.subheader('Major Wheat Producing Districts in India')
st.map(df, latitude='Latitude', longitude='Longitude', size='Wheat_Production')

st.divider()
st.header("Get services from our expert team")
col11, col12, col13 = st.columns(3)

col11.subheader("Email")
col11.markdown("iribotaqeel@gmail.com")
with col11:
    mention(label="Check project repo", icon="github", url="https://github.com/Tharunopi/Design-project-2k24")

col12.subheader("Phone")
col12.markdown("+91 93604 96536")

col13.subheader("Locate us")

m = folium.Map(location=[11.4460598, 77.7690739], zoom_start=16)
folium.Marker(
            [11.4460598, 77.7690739], popup="AgriKnow Office", tooltip="AgriKnow Office"
).add_to(m)
with col13:
    st_data = st_folium(m, width=300, height=300)