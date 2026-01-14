from app.model import AnomalyDetector

detector = AnomalyDetector("models/isolation_forest.joblib")

values = [20,21,22,100,20]
preds = detector.predict(values)

print(preds)