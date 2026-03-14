import streamlit as st
import requests
import time

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Page Config
st.set_page_config(
    page_title="YouTube Spam Detector",
    page_icon="📺",
    layout="centered"
)

# Custom CSS for Premium Look
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main {
        background-color: #0e1117;
    }

    .stHeading h1 {
        background: linear-gradient(90deg, #FF4B4B 0%, #FF8A8A 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    .stTextArea textarea {
        border-radius: 12px;
        border: 1px solid #30333d;
    }

    .stButton button {
        background: linear-gradient(90deg, #FF4B4B 0%, #FF7676 100%);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        width: 100%;
    }

    .result-card {
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        text-align: center;
        font-weight: 600;
    }

    .spam {
        background-color: rgba(255, 75, 75, 0.1);
        border: 1px solid #FF4B4B;
        color: #FF4B4B;
    }

    .not-spam {
        background-color: rgba(0, 255, 127, 0.1);
        border: 1px solid #00FF7F;
        color: #00FF7F;
    }
    </style>
""", unsafe_allow_html=True)

st.title("YouTube Spam Detector")
st.write("Analyze YouTube comments for spam using machine learning.")

comment = st.text_area("Enter Comment", placeholder="Type or paste a comment here...", height=150)

if st.button("Analyze"):
    if comment.strip():
        logger.info(f"User initiated analysis for comment: {comment[:50]}...")
        with st.spinner("Analyzing..."):
            try:
                # Use environment variable for API URL if available
                import os
                api_url = os.getenv("API_URL", "http://localhost:8000")
                res = requests.get(
                    f"{api_url}/predict",
                    params={"comment": comment},
                    timeout=5
                )
                data = res.json()
                label = data.get("label", "Unknown")
                is_spam = data.get("is_spam", False)
                
                logger.info(f"Analysis result: {label}")
                
                if is_spam:
                    st.markdown(f'<div class="result-card spam">⚠️ {label.upper()}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="result-card not-spam">✅ {label.upper()}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error("Could not connect to the API. Make sure the server is running.")
    else:
        st.warning("Please enter a comment.")