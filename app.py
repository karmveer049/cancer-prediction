import numpy as np
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("cancer_model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Convert input data to numpy array
    features = np.array(data["data"]).reshape(1, -1)

    # Check if the input has 30 features
    if features.shape[1] != 30:
        return jsonify({"error": f"Expected 30 features, but got {features.shape[1]}"})

    # Predict
    prediction = model.predict(features)

    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
