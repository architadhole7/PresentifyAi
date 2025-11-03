# 🎯 PRESENTIFYAI

**PRESENTIFYAI** is a Flask-based web application designed to generate and present content dynamically using AI models.  

---

## 🗂️ Project Structure

```text
PRESENTIFYAI/
│
│
├── static/                 # Static files (Frontend assets)
│   ├── script.js           # Handles frontend logic and user interactions
│   └── style.css           # Contains styles for HTML templates
│
├── templates/              # HTML templates used by Flask
│   ├── index.html          # Home page (input form / landing page)
│   └── result.html         # Results page (displays generated output)
│
├── venv/                   # Python virtual environment (optional, local use)
│
├── .env                    # Environment variables (API keys, secrets, etc.)
│
├── app.py                  # Main Flask application file
│
├── requirements.txt        # Python dependencies for the project
│
└── README.md               # Project documentation (you are reading it!)

```
---

##  Setup Instructions

### 1. Clone the repository


## 2. Create Virtual Environment

python -m venv venv
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate

## Install Dependencies

pip install -r requirements.txt


## Run the Flask App

python app.py








