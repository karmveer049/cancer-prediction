from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # Allow React to access API

# Load the trained model
model = joblib.load("cancer_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json['features']  # Get features from frontend
        features = np.array(data).reshape(1, -1)  # Reshape for model
        prediction = model.predict(features)  # Make prediction
        return jsonify({'prediction': int(prediction[0])})  # Send response
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Run API on port 5000
