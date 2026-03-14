import joblib
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

def evaluate_model(model_path, test_data_path):
    """
    Evaluate the trained model.
    """
    print(f"Evaluating model {model_path} with data from {test_data_path}")
    # Load model and data
    # ...
    
    # Evaluate
    # report = classification_report(y_true, y_pred)
    # print(report)

if __name__ == "__main__":
    evaluate_model("models/model.pkl", "data/processed")
