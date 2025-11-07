import joblib

print("\n🔹 Loading model and vectorizer...")
model = joblib.load("models/naive_bayes.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
print("✅ Model and vectorizer loaded successfully!\n")

# Take input from the user
text = input("📰 Enter a news article or headline to test: ")

# Transform the input text
features = vectorizer.transform([text])

# Make prediction
prediction = model.predict(features)[0]

# Output the result
if prediction == 0:
    print("\n🚨 The news is predicted to be: FAKE")
else:
    print("\n✅ The news is predicted to be: REAL")


