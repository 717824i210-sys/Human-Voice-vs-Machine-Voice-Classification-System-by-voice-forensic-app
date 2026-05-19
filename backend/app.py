from flask import Flask, request, jsonify
import joblib
import librosa

import numpy as np
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend JS to call backend

# Load model + scaler (saved with joblib)
model = joblib.load("voice_model.pkl")
scaler = joblib.load("voice_scaler.pkl")

@app.route("/")
def home():
    return "Voice Forensic Backend is running!"

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    temp_path = "temp.wav"
    file.save(temp_path)

    # Extract MFCC features
    y, sr = librosa.load(temp_path, sr=16000, mono=True)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    feat = np.mean(mfccs.T, axis=0).reshape(1, -1)
    feat_scaled = scaler.transform(feat)

    # Predict
    pred = model.predict(feat_scaled)[0]
    conf = float(np.max(model.predict_proba(feat_scaled)))

    os.remove(temp_path)

    return jsonify({
        "prediction": "Human Voice" if pred == 1 else "Machine Voice",
        "confidence": f"{conf*100:.2f}%"
    })

if __name__ == "__main__":
    app.run(debug=True)
