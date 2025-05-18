# app.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model and encoder
model = joblib.load("connectivity_model.pkl")
le = joblib.load("label_encoder.pkl")

app = FastAPI(title="School Connectivity Predictor")

class SchoolData(BaseModel):
    latitude: float
    longitude: float
    bandwidth_mbps: float
    is_urban: int

@app.post("/predict")
def predict(data: SchoolData):
    features = np.array([[data.latitude, data.longitude, data.bandwidth_mbps, data.is_urban]])
    prediction = model.predict(features)[0]
    label = le.inverse_transform([prediction])[0]
    return {"connectivity": label}
