from fastapi import FastAPI
import joblib
import os

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()

MODEL_PATH = "models/model.pkl"

def get_model():
    if os.path.exists(MODEL_PATH) and os.path.getsize(MODEL_PATH) > 0:
        try:
            return joblib.load(MODEL_PATH)
        except Exception:
            return None
    return None

model = get_model()

@app.get("/predict")
def predict(comment: str):
    logger.info(f"Received prediction request for comment: {comment[:50]}...")
    if model:
        result = model.predict([comment])
        is_spam = int(result[0]) == 1
    else:
        # Fallback logic if model is not loaded
        is_spam = "spam" in comment.lower() or "subscribe" in comment.lower()
    
    logger.info(f"Prediction: {'Spam' if is_spam else 'Not Spam'}")
    return {
        "prediction": 1 if is_spam else 0,
        "is_spam": is_spam,
        "label": "Spam" if is_spam else "Not Spam"
    }