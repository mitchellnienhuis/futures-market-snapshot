import joblib
import os

MODELS_DIR = os.path.join(os.path.dirname(__file__), "..", "models")

def load_model(name="logreg"):
    path = os.path.join(MODELS_DIR, f"{name}_model.pkl")
    try:
        return joblib.load(path)
    except:
        return None
