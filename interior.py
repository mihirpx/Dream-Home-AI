import streamlit as st
from app.model_loader import load_model
from app.utils import save_user_image
from PIL import Image
import base64
import os

# Background image function
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    ext = os.path.splitext(image_file)[1][1:]  # Get file extension without dot
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/{ext};base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def interior_page():
    # Set background
    set_background("app/assets/int.jpg")

    # Centered header using markdown
    st.markdown(
        """
        <style>
        .center-title {
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="center-title">🛋️ Interior Design Generator</div>', unsafe_allow_html=True)

    prompt = st.text_input("Describe the interior Design you want:")

    # Centered Generate button using columns
    generate_clicked = False
    col1, col2, col3 = st.columns([1, 0.5, 1])
    with col2:
        if st.button("🎨 Generate Interior Images"):
            generate_clicked = True

    # Generate images if clicked
    if generate_clicked:
        if prompt:
            with st.spinner("Generating..."):
                pipe = load_model()
                images = pipe(prompt, num_images_per_prompt=4, num_inference_steps=5).images

                for i in range(0, len(images), 2):
                    cols = st.columns(2)
                    for j in range(2):
                        if i + j < len(images):
                            with cols[j]:
                                st.image(images[i + j], caption=f"Interior Design {i + j + 1}", use_container_width=True)
                                save_user_image(st.session_state.username, prompt, images[i + j], i + j)
        else:
            st.warning("Please enter a prompt.")

    # Add vertical space to push the button to the bottom
    st.markdown("<br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

    # Back to Home button centered at the bottom
    bottom_col1, bottom_col2, bottom_col3 = st.columns([1, 2, 1])
    with bottom_col1:
        if st.button("🔙 Back to Home"):
            st.session_state.current_page = "Home"
            st.rerun()
