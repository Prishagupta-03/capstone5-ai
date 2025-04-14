# 🚦 Capstone Project 5 – DevOps-Based AI Deployment using Django & Docker

## 🔍 Project Overview

This project demonstrates the complete lifecycle of a machine learning model — from training to deployment — using open-source tools. It predicts traffic conditions (Low, Medium, High) based on vehicle count features using a Linear Regression model deployed with Django and Docker, and hosted on Render.

---

## 🛠️ Tech Stack

- **Machine Learning**: scikit-learn (Linear Regression)
- **Backend Framework**: Django
- **API Layer**: Django REST Framework
- **Serialization**: joblib (for saving ML model & label encoder)
- **Containerization**: Docker
- **Deployment**: Render (Docker-based cloud platform)
- **Version Control**: Git + GitHub

---

## 🧠 ML Model Details

- Trained on a traffic dataset (`traffic.csv`)
- Features used:
  - `CarCount`, `BikeCount`, `BusCount`, `TruckCount`
- Output:
  - `Traffic` level: `"low"`, `"medium"`, or `"high"`
- Label encoding used to convert categories → numerical values

---

## 🧪 API Usage

### 📌 Endpoint
```http
POST /api/predict/
