from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from app.model import train_model_from_csv, predict_future_sales
from app.schemas import ForecastRequest, ForecastResponse

app = FastAPI(
    title="AI Sales Forecasting API",
    description="Train and predict sales using AI",
    version="1.0.0"
)

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Sales Forecasting API running successfully"}

@app.post("/train")
async def train(file: UploadFile = File(...)):
    try:
        file_location = f"temp_{file.filename}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = train_model_from_csv(file_location)
        os.remove(file_location)

        return result

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/forecast", response_model=ForecastResponse)
def forecast(request: ForecastRequest):
    try:
        predictions = predict_future_sales(request.days)
        return {"forecast": predictions}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))