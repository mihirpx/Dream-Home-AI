import streamlit as st
from app.auth import register_user, login_user
from app.home import home_page
from app.feedback import feedback_page
from app.pages.interior import interior_page
from app.pages.exterior import exterior_page
from app.pages.floorplan import floorplan_page
from app.utils import set_custom_css

# Set page title and custom style
st.set_page_config(page_title="DreamHome AI", layout="wide")
set_custom_css()

# Initialize session state
if "auth_status" not in st.session_state:
    st.session_state.auth_status = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "current_page" not in st.session_state:
    st.session_state.current_page = "Login"

# Sidebar for authentication only
with st.sidebar:
    page = st.selectbox("🔐 Authentication", ("Login", "Register"))

    if st.session_state.auth_status:
        st.success(f"✅ Logged in as {st.session_state.username}")
        if st.button("Logout"):
            st.session_state.auth_status = False
            st.session_state.username = ""
            st.session_state.current_page = "Login"
            st.rerun()

# Registration
if page == "Register":
    registered = register_user()
    if registered:
        st.session_state.current_page = "Login"
        st.rerun()

# Login
elif page == "Login" and not st.session_state.auth_status:
    username, auth_status = login_user()
    if auth_status:
        st.session_state.auth_status = True
        st.session_state.username = username
        st.session_state.current_page = "Home"
        st.rerun()
    elif username:
        st.error("🚫 Invalid login. Please try again.")

# Main app after login
if st.session_state.auth_status:
    # Page routing based on user interaction in main area
    if st.session_state.current_page == "Home":
        home_page()
    elif st.session_state.current_page == "Interior":
        interior_page()
    elif st.session_state.current_page == "Exterior":
        exterior_page()
    elif st.session_state.current_page == "Floorplan":
        floorplan_page()
    elif st.session_state.current_page == "Feedback":
        feedback_page()
