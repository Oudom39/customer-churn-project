# Customer Churn Prediction with FastAPI

## Overview
This project predicts customer churn using the Telco dataset. The model is trained using **Scikit-learn** and deployed via **FastAPI**.

## Features
- Preprocesses customer data.
- Trains a machine learning model to predict churn.
- Deploys the model as an API using FastAPI.
- Provides a `/predict/` endpoint to get churn predictions.

---

## 🔧 Setup Instructions

1️⃣ Clone the Repository
   ```bash
   git clone https://github.com/your-username/churn-prediction.git
   cd churn-prediction
2️⃣ Create and Activate Virtual Environment
   bash
   Copy
   Edit
   python -m venv venv
   source venv/bin/activate 
3️⃣ Install Dependencies
   bash
   Copy
   Edit
   pip install -r requirements.txt
4️⃣ Train the Model
   Train the Model
   bash
   Copy
   Edit
   python src/train.py
🚀 Running the API
   Start the FastAPI server:
   bash
   Copy
   Edit
   uvicorn src.app:app --host 0.0.0.0 --port 8000
