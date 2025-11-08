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

## 🚀 Quick Start

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/meghanaepari04/Fake_News_Detector.git
cd Fake_News_Detector
2️⃣ Create and Activate a Virtual Environment
conda create -n fake_news python=3.10 -y
conda activate fake_news

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Preprocessing Script
python data_preprocessing.py


🧹 Cleans the raw dataset and prepares it for training.

5️⃣ Train the Model
python model_training.py


⚙️ Trains the Naive Bayes classifier using TF-IDF vectors.
Generates and saves:

fake_news_model.pkl

tfidf_vectorizer.pkl

6️⃣ Launch the Web App
python app.py


Now open your browser and go to:
👉 http://127.0.0.1:5000/

to test live predictions!

💡 Example Prediction

Input:

“ISRO successfully tests reusable rocket prototype.”

Output:
✅ Real News

📊 Model Overview
Component	Description
Algorithm	Multinomial Naive Bayes
Feature Extraction	TF-IDF Vectorizer
Accuracy	~90% (depends on dataset)
Libraries	scikit-learn, pandas, numpy, flask, nltk
🧾 Dataset

⚠️ The dataset is not uploaded due to GitHub’s 100 MB file size limit.

📂 Download it here:
Download Dataset

After downloading, place it inside the data/ folder before running preprocessing.

🌐 Deployment

You can easily deploy this Flask app on cloud platforms like:

Render

Railway

Heroku

Start command for deployment:

python app.py

🪪 License

This project is licensed under the MIT License
.
Feel free to use and modify with attribution. 🙌

👩‍💻 Author

Meghana Epari
🔗 GitHub Profile
