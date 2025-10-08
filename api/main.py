from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager 
import joblib
import numpy as np
import os
import time

# Global variables (or use app.state as shown later)
model = None
start_time = None

# Define lifespan using @asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI):
    global model, start_time
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f" Application started at {start_time}")

    model_path = "models/best_model.pkl"
    if not os.path.exists(model_path):
        raise RuntimeError(f"Model file not found at: {os.path.abspath(model_path)}")

    global model
    model = joblib.load(model_path)
    print("Model loaded successfully!")

    yield  # App runs here

    stop_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"Application stopped at {stop_time}")
    print(" Resources released successfully!")


# Create app WITH lifespan
app = FastAPI(title="California Housing Model API", lifespan=lifespan)


# REQUEST MODELS
class HousingFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


# ENDPOINTS
@app.get("/")
def read_root():
    return {
        "message": "California Housing Model API is running 🚀",
        "start_time": start_time
    }


@app.post("/predict")
def predict(features: HousingFeatures):
    try:
        if model is None:
            raise HTTPException(status_code=500, detail="Model not loaded.")

        data = np.array([[features.MedInc, features.HouseAge, features.AveRooms,
                          features.AveBedrms, features.Population, features.AveOccup,
                          features.Latitude, features.Longitude]])
        prediction = model.predict(data)
        return {"predicted_price": float(prediction[0])}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")