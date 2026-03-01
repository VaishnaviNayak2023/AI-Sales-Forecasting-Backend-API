import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib
from app.config import MODEL_PATH
from app.utils import ensure_model_directory
import os

def train_model_from_csv(file_path: str):
    df = pd.read_csv(file_path)

    if "sales" not in df.columns:
        raise ValueError("CSV must contain 'sales' column")

    df = df.dropna()
    df["day"] = np.arange(len(df))

    X = df[["day"]]
    y = df["sales"]

    model = LinearRegression()
    model.fit(X, y)

    ensure_model_directory()
    joblib.dump(model, MODEL_PATH)

    return {"status": "Model trained successfully"}


def predict_future_sales(days: int):
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model not trained yet")

    model = joblib.load(MODEL_PATH)
    future_days = np.arange(days).reshape(-1, 1)
    predictions = model.predict(future_days)

    return predictions.tolist()