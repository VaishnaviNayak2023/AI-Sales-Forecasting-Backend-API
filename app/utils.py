import os
from app.config import MODEL_DIR

def ensure_model_directory():
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)