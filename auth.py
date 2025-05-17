import streamlit as st
import json
import os
import hashlib
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

# Path to store user data
USER_DB = "users.json"

# -------------------------
# Helper Functions
# -------------------------

def load_users():
    if os.path.exists(USER_DB):
        with open(USER_DB, "r") as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(USER_DB, "w") as file:
        json.dump(users, file)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



# -------------------------
# Register Function
# -------------------------
def register_user():
    set_background("app/assets/registration.jpeg")

    st.markdown(
        """
        <style>
        .stApp {{
            padding: 40px;
            text-align: center;
        }}
        h1 {{
            color: white;
        }}
        label, input {{
            color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center;'>📝 Register New Account</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        username = st.text_input("Enter username")
        password = st.text_input("Enter password", type="password")
        confirm_password = st.text_input("Confirm password", type="password")

        btn_col1, btn_col2, btn_col3 = st.columns([1, 0.5, 1])
        with btn_col2:
            if st.button("Register"):
                if not username or not password:
                    st.warning("Please fill in all fields.")
                    return

                if password != confirm_password:
                    st.error("Passwords do not match.")
                    return

                users = load_users()
                if username in users:
                    st.error("Username already exists.")
                    return

                users[username] = hash_password(password)
                save_users(users)
                st.success("✅ Registration successful! You can now log in.")

# -------------------------
# Login Function
# -------------------------

def login_user():
    set_background("app/assets/image1_0.jpg")

    st.markdown(
        """
        <style>
        .stApp {{
            padding: 40px;
            text-align: center;
        }}
        h1 {{
            color: white;
        }}
        label, input {{
            color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center;'>🔐 Login to DreamHome AI</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        btn_col1, btn_col2, btn_col3 = st.columns([1, 0.5, 1])
        with btn_col2:
            if st.button("Login"):
                users = load_users()
                hashed = hash_password(password)

                if username in users and users[username] == hashed:
                    return username, True
                else:
                    st.error("Invalid username or password.")
                    return username, False

    return "", False
