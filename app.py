# app.py
from flask import Flask, render_template, request, jsonify
import joblib
import re
from text_preprocessing import clean_text

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("models/naive_bayes.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    text = clean_text(text)

    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0]
    confidence = round(proba[pred] * 100, 2)

    if pred == 1:
        result = f"✅ Real News ({confidence}% confidence)"
    else:
        result = f"🚫 Fake News ({confidence}% confidence)"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)


