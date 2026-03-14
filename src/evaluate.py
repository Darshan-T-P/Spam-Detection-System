import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
from data_ingestion import load_data
from preprocess import preprocess
from sklearn.model_selection import train_test_split

def evaluate_model(model_path):
    """
    Evaluate the trained model on the test split.
    """
    print(f"Evaluating model {model_path}...")
    
    # 1. Load Data
    df = load_data()
    X, y = preprocess(df)
    
    # 2. Get Test Split (must match the random_state/test_size from train.py)
    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Load Model
    try:
        model = joblib.load(model_path)
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    # 4. Predict and Evaluate
    y_pred = model.predict(X_test)
    
    print("\nAccuracy Score:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    evaluate_model("models/model.pkl")
