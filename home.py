import streamlit as st
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

def home_page():
    set_background("app/assets/ChatGPT Image May 10, 2025, 03_47_02 AM.png")
    st.markdown(
        """
        <style>
        .centered-title {
            text-align: center;
            font-size: 3.0em;
            font-weight: bold;
            margin-bottom: 0.2em;
        }
        .subheader {
            text-align: center;
            font-size: 1.2em;
            color: #BBBBBB;
        }
        .option-buttons {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 1.5em;
            margin-top: 2em;
        }
        .option-buttons > div {
            flex: 1 1 150px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="centered-title">🏡 Welcome to DreamHome AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Design your dream space with the power of AI</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("##  DreamHome AI")

    st.markdown("""
    DreamHome AI is a smart design assistant powered by cutting-edge AI models such as **Stable Diffusion** and **Pix2Pix GANs**. Whether you're dreaming of a cozy bedroom, a modern kitchen, a futuristic house exterior, or a detailed architectural floor plan — we've got you covered.

    This app empowers homeowners, architects, designers, and real estate enthusiasts to:

    - 🧱 **Visualize designs** before actual construction or renovation
    - 🖼️ **Generate multiple design ideas** from simple text prompts
    - 📐 **Create smart and creative floor plan layouts**
    - 💡 **Explore inspiration** for interior and exterior themes

    With AI doing the heavy lifting, you can focus on what truly matters — your creativity and vision.
    """)

    st.markdown("---")

    st.markdown("---")
    st.markdown("## 👉 Select an option to get started:")

    # Button layout using columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🛋️ Interior", use_container_width=True):
            st.session_state.current_page = "Interior"
            st.rerun()

    with col2:
        if st.button("🏞️ Exterior", use_container_width=True):
            st.session_state.current_page = "Exterior"
            st.rerun()

    with col3:
        if st.button("📐 Floorplan", use_container_width=True):
            st.session_state.current_page = "Floorplan"
            st.rerun()

    with col4:
        if st.button("💬 Feedback", use_container_width=True):
            st.session_state.current_page = "Feedback"
            st.rerun()

    st.markdown("---")



