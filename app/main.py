from fastapi import FastAPI
from app.model import AnomalyDetector
from typing import List
from pydantic import BaseModel
from app.rules import apply_rules

app = FastAPI(title="AIOps Anomaly Detector API")


# Load the model once you start the app
detector = AnomalyDetector("models/isolation_forest.joblib")


# request schema
class PredictionRequest(BaseModel):
    values:List[float]



# Routers
@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def health_check():
    return {"status":"API is running"}


@app.post("/predict")
def predict(requests: PredictionRequest):
    """
    Expected Payload
    
    values = [20,30,20,21,22,25,80,23]
    """
    values = requests.values

    ml_predictions = detector.predict(values)

    rule_predictions = apply_rules(values)

    # Combine result

    final_anomalies = [
        -1 if (ml == -1 or rule == -1) else 1
        for ml, rule in zip(ml_predictions, rule_predictions)
    ]

    return {
        "values" : values,
        "ml_anomalies" : ml_predictions,
        "rule_anomalies" : rule_predictions,
        "final_anomalies" : final_anomalies
    }