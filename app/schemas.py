from pydantic import BaseModel
from typing import List

class ForecastRequest(BaseModel):
    days: int

class ForecastResponse(BaseModel):
    forecast: List[float]