from flask import Flask, request, jsonify
from utils import load_model, predict_image

app = Flask(__name__)
model = load_model()

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    pred, score = predict_image(model, image)
    
    return jsonify({
        "prediction": pred,
        "confidence": float(score)
    })
