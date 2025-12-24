import json
import joblib
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load artifacts
SCALER = joblib.load("model/scaler.joblib")
MODEL = joblib.load("model/model.joblib")
with open("model/feature_names.json", "r") as f:
    FEATURE_NAMES = json.load(f)

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.post("/predict")
def predict():
    """
    Expected JSON body:
    {
      "age": 63,
      "sex": 1,
      ...
    }
    Keys must match FEATURE_NAMES.
    
    """
    
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    # Ensure all features exist
    missing = [k for k in FEATURE_NAMES if k not in data]
    if missing:
        return jsonify({"error": "Missing features", "missing": missing}), 400

    # Build input in correct order
    x = np.array([[float(data[k]) for k in FEATURE_NAMES]], dtype=float)
    x_scaled = SCALER.transform(x)

    # Probability for class 1 (disease)
    proba = float(MODEL.predict_proba(x_scaled)[0][1])
    pred = int(proba >= 0.5)

    return jsonify({
        "prediction": pred,              # 1 disease risk, 0 no risk
        "probability": round(proba, 4),  # risk probability
        "threshold": 0.5
    })

if __name__ == "__main__":
    # For mobile testing, run on LAN IP: host="0.0.0.0"
    app.run(host="0.0.0.0", port=5000, debug=True)
