import streamlit as st
import pandas as pd

st.logo(r"C:\Users\tharu\OneDrive\Pictures\Screenshots 1\Screenshot 2024-07-13 144102.png")
home_page = st.Page("first.py", title="home", icon=":material/add_circle:")
cnn_page = st.Page("AAcnn_model.py", title="cnn", icon=":material/add_circle:")
chatbot = st.Page("Chatbot.py", title="Chatbot", icon=":material/delete:")
model = st.Page("model.py", title="model", icon=":material/add_circle:")
model2 = st.Page("model2.py", title="model2", icon=":material/delete:")
tech = st.Page("Data_alteration.py", title="Tech", icon=":material/delete:")

pg = st.navigation([home_page, cnn_page, chatbot, model, model2, tech])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()

