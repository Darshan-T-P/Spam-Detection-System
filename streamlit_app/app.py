import streamlit as st
import requests

st.set_page_config(page_title="YouTube Spam Detector", layout="centered")

st.title("📺 YouTube Spam Comment Detector")
st.markdown("Check if a YouTube comment is spam or not.")

comment_text = st.text_area("Enter YouTube comment:", placeholder="Type here...")

if st.button("Predict"):
    if comment_text:
        # Placeholder for API call
        # response = requests.post("http://api:8000/predict", json={"text": comment_text})
        # prediction = response.json()["is_spam"]
        st.info("Prediction functionality will be implemented soon.")
    else:
        st.warning("Please enter some text.")
