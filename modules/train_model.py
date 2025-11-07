# modules/train_model.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

print("🔹 Loading cleaned dataset...")
df = pd.read_csv("data/cleaned_dataset.csv")

X = df["clean_content"]
y = df["label"]

print(f"✅ Dataset loaded. Shape: {df.shape}")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorization
print("🔹 Extracting features using TF-IDF...")
vectorizer = TfidfVectorizer(max_features=10000, stop_words="english", ngram_range=(1,2))
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Model training
print("🧠 Training Naive Bayes model...")
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Evaluate
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n✅ Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save
joblib.dump(model, "models/naive_bayes.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")
print("\n💾 Model and vectorizer saved successfully!")

