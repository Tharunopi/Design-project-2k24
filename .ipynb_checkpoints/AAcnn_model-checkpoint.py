import tensorflow as tf
import time
import streamlit as st
from PIL import Image
import numpy as np
from keras.preprocessing import image
model = tf.keras.models.load_model("mobilenet.h5")
indives = {0:'Brown_rust', 1:'Healthy', 2:'Yellow_rust'}
st.title("Image prediction model")
st.logo(r"C:\Users\tharu\OneDrive\Pictures\Screenshots 1\Screenshot 2024-07-13 144102.png")
raw_data = st.file_uploader("choose an image file", accept_multiple_files=False)
if raw_data is not None:
    img = Image.open(raw_data)
    img = img.resize((224, 224)) 
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    st.image(raw_data, "uploaded image")
    
    def page2():
        st.title("Description")
        placeholder = st.empty()
    
        full_text = """A healthy wheat leaf is a vital indicator of the overall health and potential yield of the wheat plant. 
    
    Color: The leaf should display a vibrant green color, ranging from light to dark green depending on the wheat variety and growth stage.
    
    Structure: A healthy leaf is typically long, narrow, and blade-like. It should be firm and stand upright, showing good turgor pressure.
    
    Surface: The leaf surface should be smooth and free from any spots, lesions, or discolorations. There should be no signs of wilting or curling.
    
    Venation: Clear, parallel veins should be visible running the length of the leaf, indicating good vascular health.
    
    Margins: The leaf edges should be intact, without any signs of damage or irregularities.
    
    Growth: New leaves should be emerging regularly, showing consistent growth and development of the plant.
    
    Absence of pests: There should be no visible signs of insect activity or damage, such as holes or chew marks.
    
    Free from disease: No symptoms of common wheat diseases like rust (brown or yellow patches), powdery mildew (white, fluffy patches), or septoria (brown spots     with yellow halos) should be present.
    
    A healthy wheat leaf is crucial for photosynthesis, allowing the plant to produce the energy needed for growth and grain production. Regular monitoring of        leaf health is an essential practice in wheat cultivation."""
    
        displayed_text = ""
        for char in full_text:
            displayed_text += char
            placeholder.markdown(displayed_text + "▌")
            time.sleep(0.02) 
    
        placeholder.markdown(displayed_text)

        sentiment_mapping = ["one", "two", "three", "four", "five"]
        selected = st.feedback("stars")
        if selected is not None:
            st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

        
    def predict():
        result = (model.predict(img_array))[0]
        for i,j in enumerate(result):
            if j == 1:
                resul = indives[i]
                with st.spinner('Your Image is cooking🦇'):
                    time.sleep(2)
                with st.container():
                    st.error(indives[i], icon="✅")
                    st.button("Check full details", on_click=page2)
                    
    st.button("predict", on_click=predict)
    st.divider()
