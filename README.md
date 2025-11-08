<h1 align="center">📰 Fake News Detection System</h1>

<p align="center">
Detect fake news using <b>Machine Learning</b>, <b>TF-IDF Vectorization</b>, and a <b>Naive Bayes Classifier</b>.<br>
A complete end-to-end NLP + Flask web app for real-time news verification.
</p>

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python Badge">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Flask-2.3-lightgrey" alt="Flask Badge">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Machine%20Learning-Enabled-yellow" alt="ML Badge">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/NLP-TF--IDF-orange" alt="NLP Badge">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License Badge">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Status-Active-success" alt="Active Status Badge">
  </a>
</p>

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
🚀 Quick Start
🧩 1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/meghanaepari04/Fake_News_Detector.git
cd Fake_News_Detector
⚙️ 2️⃣ Create and Activate a Virtual Environment
bash
Copy code
# Create environment
conda create -n fake_news python=3.10 -y
conda activate fake_news
📦 3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
🧹 4️⃣ Run Preprocessing Script
bash
Copy code
python data_preprocessing.py
🧼 Cleans the raw dataset and prepares it for training.

🧠 5️⃣ Train the Model
bash
Copy code
python model_training.py
✅ Trains the Naive Bayes classifier using TF-IDF vectors.
It generates and saves:

Copy code
fake_news_model.pkl  
tfidf_vectorizer.pkl  
🌐 6️⃣ Run the Flask Web App
bash
Copy code
python app.py
Now open your browser and visit:
👉 http://127.0.0.1:5000/

to access the Fake News Detection interface.

💡 Example Prediction
Input:

"ISRO successfully tests reusable rocket prototype."

Output:
✅ Real News

📊 Model Overview
Component	Description
Algorithm	Multinomial Naive Bayes
Feature Extraction	TF-IDF Vectorizer
Accuracy	~90% (depends on dataset)
Libraries Used	scikit-learn, pandas, numpy, flask, nltk

🧾 Dataset
⚠️ The dataset is not included in this repository due to GitHub’s file size limitations.

📂 You can download the dataset from Kaggle:
👉 Download Dataset

After downloading, place it inside the data/ folder before running:

bash
Copy code
python data_preprocessing.py
🌐 Deployment
You can easily deploy this Flask app on cloud platforms such as:

Render

Railway

Heroku

Start Command:

bash
Copy code
python app.py
🪪 License
This project is licensed under the MIT License.
You’re free to use and modify this project with attribution.

👩‍💻 Author
Meghana Epari
🔗 GitHub Profile

yaml
Copy code

---

You're all set ✨  
Just paste this into your `README.md` file on GitHub and enjoy the clean, professional project display 🙌  

Need a version with **dark mode preview / live demo GIFs** added too? Just let me know!







