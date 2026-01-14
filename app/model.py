import joblib
import numpy as np



class AnomalyDetector:

    def __init__(self, model_path:str):
        self.model = joblib.load(model_path)

    def predict(self, values):
        """
        Docstring for predict
        
        :values: list of floats
        :return: list of anomaly labels -1 or 1
        """

        X = np.array(values).reshape(-1,1)
        return self.model.predict(X).tolist()