import streamlit as st
import pandas as pd
from datetime import datetime
import time


st.title("Welcome to AI assitant")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
now = datetime.now()
col4.text(f"Today's date: {now.strftime('%Y-%m-%d')}")
col4.text(f"Session login time: {now.strftime('%H:%M:%S')}")
col4.image(r"agri_logo.png", width=200)
  
# st.divider()
tab1, tab2, tab3 = st.tabs(["Overview", "Technology", "Key features"])



with tab1:
    st.subheader("Overview")
    st.markdown("By leveraging machine learning (ML) models, a Convolutional Neural Network (CNN), and a chatbot interface, farmers can receive real-time insights and recommendations tailored to their specific farming needs.")

    st.image(r"ai wheat.jpg", width=500)

with tab2:
    st.subheader("Technologies Used")
    st.markdown("Machine Learning: Random Forest, Gradient Boosting")
    st.markdown("Deep Learning: CNN (MobileNet)")
    st.markdown("Chatbot Integration: Gemini API")
    st.markdown("Future Integration: YOLO (object detection), Sign-based LLM")
    st.image(r"ai wheat2.jpg", width=500)

with tab3:
    st.subheader("Key features")
    st.markdown("Yield Prediction")
    st.link_button("Go to yied prediction model", "")
    st.caption("This navigate to prediction page")
    st.markdown("Disease Detection")
    st.link_button("Go to disease prediction model", "")
    st.caption("This navigate to prediction cnn model page")
    st.markdown("Farmer Chatbot")
    st.link_button("Go to Chatbot to get assitant", "")
    st.caption("This navigate to chatbot page")

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
col11, col12 = st.columns(2)

col11.subheader("Email")
col11.markdown("iribotaqeel@gmail.com")

col12.subheader("Phone")
col12.markdown("+91 93604 96536")