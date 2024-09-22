import streamlit as st
import pandas as pd

home_page = st.Page("first.py", title="Home")
cnn_page = st.Page("AAcnn_model.py", title="CNN")
chatbot = st.Page("Chatbot.py", title="Chatbot")
model = st.Page("model.py", title="Model-1")
model2 = st.Page("model2.py", title="Model-2")
tech = st.Page("Data_alteration.py", title="Datasets")
profile = st.Page("profile.py", title="Profile")

pg = st.navigation([home_page, cnn_page, chatbot, model, model2, tech, profile])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:", layout="wide")
pg.run()

