import joblib

model_path = 'random_forest_model.pkl'

try:
    with open(model_path, 'rb') as f:
        model = joblib.load(f)
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading the model:", e)
