import streamlit as st
import os
from PIL import Image

def set_custom_css():
    st.markdown("""
        <style>
        /* App background and text */
        body {
            background-color: #121212;
            color: #f5f5f5;
        }

        /* Main content background */
        .stApp {
            background-color: #1e1e1e;
        }

        /* Headings and labels */
        h1, h2, h3, h4, h5, h6 {
            color: #e0e0e0;
        }

        /* Input fields and buttons */
        .stTextInput > div > div > input,
        .stButton button {
            background-color: #333333;
            color: white;
            border: 1px solid #444;
        }

        .stButton button:hover {
            background-color: #555555;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #2c2c2c;
        }

        /* Warnings, errors, success */
        .stAlert {
            background-color: #333 !important;
            color: #fdd835 !important;
        }
        </style>
    """, unsafe_allow_html=True)



def save_user_image(username, prompt, image, index):
    user_dir = os.path.join("generated_images", username)
    os.makedirs(user_dir, exist_ok=True)
    filename = f"{prompt.replace(' ', '_')}_{index + 1}.png"
    filepath = os.path.join(user_dir, filename)
    image.save(filepath)

