from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__, static_folder="frontend/build", static_url_path="")
CORS(app)

# Load the trained model
model = pickle.load(open("cancer_model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    prediction = model.predict([np.array(data)])
    return jsonify({"prediction": int(prediction[0])})

# Serve React frontend
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists("frontend/build/" + path):
        return send_from_directory("frontend/build", path)
    else:
        return send_from_directory("frontend/build", "index.html")

if __name__ == "__main__":
    app.run(debug=True)
