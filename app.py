# from flask import Flask, request, jsonify
# import joblib

# app = Flask(__name__)

# # Load trained model
# model = joblib.load('random_forest_model.pkl')

# @app.route('/')
# def index():
#     return app.send_static_file('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get input data
#     data = request.json
#     # Preprocess input data (convert to DataFrame, perform any necessary transformations)
#     # Perform prediction
#     prediction = model.predict(data)
#     # Return prediction
#     return jsonify({'prediction': prediction})

# if __name__ == '__main__':
#     app.run(debug=True)

########################

# from flask import Flask, request, jsonify
# import joblib
# import os

# app = Flask(__name__)

# # Load trained model
# model_path = 'random_forest_model.pkl'
# if os.path.exists(model_path):
#     model = joblib.load(model_path)
# else:
#     raise FileNotFoundError(f"Model file '{model_path}' not found.")

# @app.route('/')
# def index():
#     return app.send_static_file('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get input data
#     data = request.json
#     # Preprocess input data (convert to DataFrame, perform any necessary transformations)
#     # Perform prediction
#     prediction = model.predict(data)
#     # Return prediction
#     return jsonify({'prediction': prediction})

# if __name__ == '__main__':
#     app.run(debug=True)

#################################################

from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Define the path to the trained model
MODEL_PATH = 'random_forest_model.pkl'

# Check if the model file exists
if not os.path.exists(MODEL_PATH):
    print(f"Error: Model file '{MODEL_PATH}' not found.")
    exit(1)

# Load trained model
try:
    with open(MODEL_PATH, 'rb') as f:
        model = joblib.load(f)
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading the model:", e)  # Print full error message
    exit(1)

@app.route('/')
def index():
    return app.send_static_file('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get input data
#         data = request.json
#         # Log input data received
#         print('Input data received:', data)
#         # Preprocess input data (convert to DataFrame, perform any necessary transformations)
#         # Perform prediction
#         prediction = model.predict(data)
#         # Log prediction result
#         print('Prediction result:', prediction)
#         # Return prediction
#         return jsonify({'prediction': prediction})
#     except Exception as e:
#         # Log any errors that occur during prediction
#         print('Prediction error:', e)
#         return jsonify({'error': str(e)})

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get input data
#         data = request.json
#         # Log input data received
#         print('Input data received:', data)
        
#         # Convert categorical variables to numerical using label encoding
#         categorical_columns = ['protocol_type', 'service', 'flag']
#         label_encoders = {}
#         for col in categorical_columns:
#             data[col] = label_encoders[col].transform([data[col]])[0]
        
#         # Preprocess input data (convert to DataFrame, perform any necessary transformations)
#         # Perform prediction
#         prediction = model.predict([list(data.values())])
        
#         # Log prediction result
#         print('Prediction result:', prediction)
#         # Return prediction
#         return jsonify({'prediction': prediction[0]})
#     except Exception as e:
#         # Log any errors that occur during prediction
#         print('Prediction error:', e)
#         return jsonify({'error': str(e)})

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get input data
#         data = request.json
        
#         # Log input data received
#         print('Input data received:', data)
        
#         # Preprocess input data (convert to DataFrame, perform any necessary transformations)
        
#         # Perform prediction
#         prediction = model.predict(data)
        
#         # Log prediction result
#         print('Prediction result:', prediction)
        
#         # Return prediction
#         return jsonify({'prediction': prediction})
#     except Exception as e:
#         # Log any errors that occur during prediction
#         print('Prediction error:', e)
#         return jsonify({'error': str(e)})
import pandas as pd
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data
        data = request.json
        # Log input data received
        print('Input data received:', data)
        # Preprocess input data (convert to DataFrame, perform any necessary transformations)
        # Convert input data to DataFrame
        input_df = pd.DataFrame(data)
        
        # Preprocess input data (perform any necessary transformations)
        # Example: You might need to handle categorical variables or scale numerical features
        
        # Perform prediction
        prediction = model.predict(input_df)
        # Log prediction result
        print('Prediction result:', prediction)
        # Return prediction
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        # Log any errors that occur during prediction
        print('Prediction error:', e)
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)