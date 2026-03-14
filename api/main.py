from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="YouTube Spam Detection API")

# Load model (placeholder)
# model = joblib.load("models/model.pkl")

class Comment(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "YouTube Spam Detection API is running"}

@app.post("/predict")
def predict_spam(comment: Comment):
    # Placeholder logic
    # prediction = model.predict([comment.text])
    return {"text": comment.text, "is_spam": False}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
