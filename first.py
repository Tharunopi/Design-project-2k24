import streamlit as st
import pandas as pd


st.title("Welcome to iribot")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
st.divider()
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
    'District': ['District1', 'District2', 'District3'],
    'Latitude': [20.5937, 26.8467, 28.6139],
    'Longitude': [78.9629, 80.9462, 77.2090],
    'Wheat_Production': [100000, 150000, 200000]
}

df = pd.DataFrame(data)

st.subheader('Major wheat Producing Districts in India')
st.map(df, latitude='Latitude', longitude='Longitude', size='Wheat_Production')

st.divider()
st.header("Get services from our expert team")
col11, col12 = st.columns(2)

col11.subheader("Email")
col11.markdown("iribotaqeel@gmail.com")

col12.subheader("Phone")
col12.markdown("+91 93604 96536")