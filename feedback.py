import streamlit as st
import datetime
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

def feedback_page():
    set_background("app/assets/feed1.jpg")
    st.title("💬 Feedback")

    st.markdown("We value your feedback! Please share your thoughts below:")

    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        experience = st.radio("How was your experience?", ["Excellent", "Good", "Average", "Poor"])
        comments = st.text_area("Additional Comments")
        submitted = st.form_submit_button("Submit Feedback")

        if submitted:
            if name and email:
                # Save feedback to a text file
                feedback_entry = (
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Experience: {experience}\n"
                    f"Comments: {comments}\n"
                    f"Submitted on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                    "-------------------------\n"
                )

                with open("feedback.txt", "a") as f:
                    f.write(feedback_entry)

                st.success("✅ Thank you for your feedback!")
                st.info(f"🗓️ Submitted on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                st.warning("⚠️ Please fill in at least your name and email.")

    st.markdown("---")
    if st.button("Back to Home"):
        st.session_state.current_page = "Home"
        st.rerun()
