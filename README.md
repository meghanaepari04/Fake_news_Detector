<h1 align="center">📰 Fake News Detection System</h1>

<p align="center">
Detect fake news using <b>Machine Learning</b>, <b>TF-IDF Vectorization</b>, and a <b>Naive Bayes Classifier</b>.  
A complete end-to-end NLP + Flask web app for real-time news verification.
</p>

---

## ⚡ Preview

> 🚀 Input a news headline or paragraph → Get instant prediction: **Real ✅** or **Fake ❌**

---

## 📘 About the Project

Fake news spreads rapidly on digital platforms, and distinguishing real from fake information is increasingly challenging.  
This project uses **Natural Language Processing (NLP)** techniques and **machine learning algorithms** to automatically classify news articles as *real* or *fake*.

Built with ❤️ using **Python**, **scikit-learn**, and **Flask**.

---

## 🧠 Features

- 🧹 Cleans and preprocesses text (stopwords, punctuation, case normalization)  
- ✨ Extracts features using **TF-IDF Vectorization**  
- 🧮 Classifies news using **Naive Bayes Algorithm**  
- 🌐 Flask web app for live detection  
- 🔍 Easy to retrain with your own dataset  

---

## 🗂️ Project Structure

```bash
Fake_News_Detector/
│
├── data/                     # Dataset folder (excluded from GitHub)
├── model/                    # Saved model and vectorizer
├── static/                   # CSS for Flask app
├── templates/                # HTML files for web UI
│
├── app.py                    # Flask backend
├── data_preprocessing.py     # Script for text cleaning
├── model_training.py         # Script for training the model
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
└── LICENSE                   # MIT License

