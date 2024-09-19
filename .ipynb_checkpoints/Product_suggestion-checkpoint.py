import streamlit as st
import requests
from PIL import Image
import os 

GEMINI_API_KEY = "AIzaSyDGNQGAq9o1_3-tDBwyPtUsGlj9k6XuDFk"
GEMINI_API_ENDPOINT = 'https://api.gemini.com/v1/product_recognition'

def get_product_details(image_path):
    """Send image to Gemini API and get product details."""
    headers = {
        'Authorization': f'Bearer {GEMINI_API_KEY}',
        'Content-Type': 'application/octet-stream'
    }
    with open(image_path, 'rb') as image_data:
        response = requests.post(GEMINI_API_ENDPOINT, headers=headers, data=image_data)
        response.raise_for_status() 
        return response.json()

def main():
    st.title("Product Recognition Chatbot")
    st.write("Upload an image to identify products and get details.")

    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        temp_dir = 'temp_uploads'
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        
        image_path = os.path.join(temp_dir, uploaded_file.name)
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.image(Image.open(image_path), caption='Uploaded Image', use_column_width=True)

        try:
            product_details = get_product_details(image_path)
            
            st.subheader("Product Details:")
            if product_details:
                for product in product_details.get('products', []):
                    st.write(f"Name: {product.get('name')}")
                    st.write(f"Price: {product.get('price')}")
                    st.write(f"Description: {product.get('description')}")
                    st.write(f"Category: {product.get('category')}")
                    st.write("---")
            else:
                st.write("No products found in the image.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error calling the Gemini API: {e}")

if __name__ == "__main__":
    main()
