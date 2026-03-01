# AI Sales Forecasting Backend

This repository contains a **FastAPI backend** for training and predicting sales using a simple AI/ML model. 
It allows uploading CSV sales data, training a Simple Linear Regression model, and generating future forecasts.

⚠️ **Note:** This is a **simple model for learning and demonstration purposes only**. It is not intended for production use or highly accurate forecasting.

## 🚀 Features

- **Train Model**: Upload a CSV file with sales data to train a forecasting model.
- **Forecast Sales**: Generate forecasts for a specified number of future days.
- **Swagger UI**: Interactive API documentation available at `/docs`.
- **CORS Enabled**: Ready to be connected with a frontend like React.

## 🛠️ Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- Pandas, NumPy, scikit-learn, joblib
- Optional: Virtual environment recommended

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/VaishnaviNayak2023/AI-Sales-Forecasting-Backend-API.git
cd AI-Sales-Forecasting-Backend-API/backend
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🏃 Running the Backend

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

* API base URL: `http://localhost:8000`
* Swagger UI (interactive docs): `http://localhost:8000/docs`

### Endpoints

* `POST /train` → Upload a CSV to train the model (must include a `sales` column)
* `POST /forecast` → Generate forecasts for a specified number of future days

## 📁 Folder Structure

```
backend/
├─ app/
│  ├─ main.py        # FastAPI app entry point
│  ├─ model.py       # Training and forecasting logic
│  ├─ schemas.py     # Pydantic schemas for request/response
│  ├─ utils.py       # Utility functions
│  └─ config.py      # Model paths and directories
├─ requirements.txt
└─ README.md
```

## 📝 Usage

### Train Model

1. Send a **POST** request to `/train` with a CSV file containing a `sales` column.
2. Example response:

```json
{
  "status": "Model trained successfully"
}
```

### Forecast

1. Send a **POST** request to `/forecast` with a JSON body like:

```json
{
  "days": 7
}
```

2. Example response:

```json
{
  "forecast": [100, 120, 130, ...]
}
```

## ⚠️ Notes

* This backend uses a **simple Linear Regression model**; forecasts follow a linear trend.
* Forecasts currently start from day 0 of the model. Future improvements can include:

  * Storing the last training day so forecasts continue correctly
  * Using more advanced forecasting models (ARIMA, Prophet, LSTM, etc.) for better accuracy
  * Ensure CSV files include a `sales` column and contain no missing values.

## 🔗 Useful Links

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Uvicorn Documentation](https://www.uvicorn.org/)
* [GitHub Repository](https://github.com/VaishnaviNayak2023/AI-Sales-Forecasting-Backend-API)

---

This backend is fully functional as a starting point for AI sales forecasting, with room for enhancements in prediction accuracy and continuity.
