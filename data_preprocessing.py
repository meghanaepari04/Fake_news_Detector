# data_preprocessing.py
import pandas as pd
import re
import os

def clean_text(text):
    """Clean text by removing URLs, punctuation, and extra spaces."""
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text

print("🔹 Loading dataset...")

# ✅ Use the correct filename (capital D)
DATA_PATH = "data/Dataset.csv"

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"❌ File not found: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

# ✅ Check for required columns
required_columns = ["title", "text", "label"]
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"❌ Column '{col}' missing in Dataset.csv")

# ✅ Combine title + text
df["content"] = df["title"].fillna("") + " " + df["text"].fillna("")

# ✅ Clean text content
print("🧹 Cleaning text...")
df["clean_content"] = df["content"].apply(clean_text)

# ✅ Normalize labels (convert to 0=fake, 1=real)
df["label"] = df["label"].astype(str).str.lower().map({
    "fake": 0, "false": 0, "0": 0,
    "real": 1, "true": 1, "1": 1
}).fillna(0).astype(int)

# ✅ Drop empty rows
df = df[df["clean_content"].str.strip() != ""]

# ✅ Save cleaned dataset
os.makedirs("data", exist_ok=True)
cleaned = df[["clean_content", "label"]]
cleaned.to_csv("data/cleaned_dataset.csv", index=False)

print("✅ Cleaned dataset saved at 'data/cleaned_dataset.csv'")
print("📊 Shape:", cleaned.shape)
print("🔖 Label distribution:\n", cleaned["label"].value_counts())
