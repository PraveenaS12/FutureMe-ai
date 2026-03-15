FutureMe AI ✨
AI-Powered Lifestyle Forecaster - Predicts your focus, energy, productivity & burnout risk 1-5 years ahead based on daily habits using Machine Learning.

🎯 Features
Interactive Dashboard - Real-time sliders for sleep/study/exercise habits

ML Predictions - RandomForest model trained on 1000+ data points

Future Simulations - Project outcomes 1-5 years ahead

Visual Analytics - Dynamic radar charts (Chart.js)

AI Chatbot - Personalized habit improvement advice

REST API - Production-ready Flask backend

📋 Table of Contents
Installation

Quick Start

Project Structure

API Endpoints

Demo

Tech Stack

Future Enhancements

🚀 Quick Start
bash
# 1. Clone & Install
git clone https://github.com/PraveenaS12/FutureMe-ai.git
cd futureme-ai
pip install -r requirements.txt

# 2. Train Model
python scripts/generate_data.py
python scripts/train_model.py

# 3. Run Backend
python backend/app.py
Open frontend/index.html in browser 🎉

🛠️ Installation
Prerequisites: Python 3.8+

Clone repo:

bash
git clone https://github.com/PraveenaS12/FutureMe-ai.git
cd futureme-ai
Virtual Environment:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install Dependencies:

bash
pip install -r requirements.txt
Generate Dataset & Train:

bash
python scripts/generate_data.py
python scripts/train_model.py
Start Server:

bash
python backend/app.py
📁 Project Structure
text
futureme-ai/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── .gitignore            # Git exclusions
├── backend/
│   └── app.py           # Flask REST API
├── frontend/             # Client-side app
│   ├── index.html
│   ├── style.css
│   └── script.js
├── model/
│   └── dataset.csv      # Training data (1000+ rows)
└── scripts/             # ML Pipeline
    ├── generate_data.py
    └── train_model.py
🌐 API Endpoints
Method	Endpoint	Description
POST	/predict	Get future predictions
POST	/chat	AI habit improvement advice
Sample /predict Request:

json
{
  "sleep": 7, "study": 3, "screen": 5,
  "exercise": 1, "stress": 4, "futureYear": 2
}
📊 Demo
Adjust sliders → Instant predictions → Personalized advice!

(Add screenshot: `Demoafter taking one)*

🛠️ Tech Stack
Category	Technology
Backend	Flask, CORS
Machine Learning	scikit-learn, RandomForest
Frontend	HTML5, CSS3, Chart.js
Data	Pandas, CSV
Deployment	GitHub Pages
🎯 Future Enhancements
 PyTorch neural network upgrade

 Real-time database (SQLite/PostgreSQL)

 Mobile-responsive design

 User authentication & history

 Docker containerization



👤 Built by Praveena Subramanian
AI/ML Engineering Student | Chennai
March 202
