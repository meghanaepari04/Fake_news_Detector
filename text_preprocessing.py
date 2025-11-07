# text_preprocessing.py
import re

def clean_text(text):
    """Clean input text for predictions."""
    if not isinstance(text, str):
        text = str(text)
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text

