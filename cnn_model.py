import tensorflow as tf
import streamlit as st
from PIL import Image
import numpy as np
from keras.preprocessing import image

model = tf.keras.models.load_model("mobilenet.h5")
indives = {0:'Brown_rust', 1:'Healthy', 2:'Yellow_rust'}

st.title("Image prediction model")

st.image(r"C:\Users\tharu\OneDrive\Pictures\Screenshots 1\Screenshot 2024-07-13 144102.png", "Beloved company")

raw_data = st.file_uploader("choose an image file", accept_multiple_files=False)

if raw_data is not None:
    img = Image.open(raw_data)
    img = img.resize((224, 224)) 
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    def predict():
        result = (model.predict(img_array))[0]
        for i,j in enumerate(result):
            if j == 1:
                st.success(indives[i])
        
    st.button("predict", on_click=predict)