AIOps Anomaly Detection ML System

An end-to-end AIOps anomaly detection system designed to identify abnormal patterns in system and operational metrics using unsupervised machine learning and rule-based heuristics, with a production-ready inference API.

🚀 Project Overview

This project implements an unsupervised anomaly detection pipeline using Isolation Forest, combined with domain-driven rule-based checks, to detect abnormal behavior in system metrics.
The trained model is exposed via a FastAPI REST endpoint, containerized with Docker, and deployed using AWS Fargate (ECS) for scalable, serverless inference.

🧠 Key Features

Unsupervised anomaly detection using Isolation Forest

Feature engineering, scaling, and anomaly scoring

Hybrid approach combining ML-based detection + rule-based heuristics

FastAPI-based inference service

Dockerized application for reproducible deployment

Cloud deployment using AWS Fargate

Consideration of data drift, retraining cadence, and model versioning

🛠️ Tech Stack

Language: Python 3.12

ML / Data: Scikit-learn, Pandas, NumPy

API: FastAPI

Containerization: Docker

Cloud: AWS Fargate (ECS)

Model Serialization: Joblib

📁 Project Structure
AIOPS-ANOMALY-DETECTION/
│
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── model.py             # Model loading & inference logic
│   ├── rules.py             # Rule-based anomaly heuristics
│   └── __init__.py
│
├── models/
│   └── isolation_forest.joblib   # Trained Isolation Forest model
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_anomaly_data_exploration.ipynb
│   ├── 03_EDA.ipynb
│   └── 04_realtime_testing.ipynb
│
├── test_model.py            # Basic model testing & validation
├── requirements.txt         # Project dependencies
├── Dockerfile               # Docker configuration
└── README.md

⚙️ How It Works

Data Exploration & EDA
Conducted exploratory analysis to understand metric distributions, patterns, and anomalies.

Feature Engineering & Modeling
Engineered relevant features and trained an Isolation Forest model for unsupervised anomaly detection.

Hybrid Detection Logic
Combined model predictions with rule-based thresholds to improve robustness and reduce false positives.

Inference API
Exposed anomaly predictions via a FastAPI endpoint, returning anomaly flags and scores.

Deployment
Containerized the application with Docker and deployed on AWS Fargate for scalable inference.

▶️ Running Locally
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Start FastAPI Server
uvicorn app.main:app --host 0.0.0.0 --port 8000

3️⃣ API Documentation

Access Swagger UI at:

http://localhost:8000/docs

🐳 Docker Usage
Build Image
docker build -t aiops-anomaly-detector .

Run Container
docker run -p 8000:8000 aiops-anomaly-detector

☁️ Deployment (AWS Fargate)

Docker image deployed via Amazon ECS with Fargate

Serverless container execution

Scalable inference without managing servers

(Free Tier–friendly setup used for learning and experimentation)

📊 Model Considerations

Unsupervised learning (no labeled anomalies required)

Awareness of data drift

Planned retraining cadence

Basic model versioning strategy

📌 Use Cases

Infrastructure monitoring

System health analytics

AIOps & SRE support

Early anomaly detection in operational metrics

🔮 Future Enhancements

Automated retraining pipeline

Metrics monitoring & alerting

Model performance dashboards

Streaming data support

👤 Author

Built as part of a hands-on ML / MLOps learning project to demonstrate real-world anomaly detection, deployment, and cloud-native inference.