import joblib
import logging
import os
from datetime import datetime
from typing import List, Optional
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from schemas import PredictRequest

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
MODEL_BASE = os.path.join(os.path.dirname(APP_ROOT), "models")

MODEL_VERSION = os.environ.get("MODEL_VERSION", "v1")
MODEL_PATH = os.path.join(MODEL_BASE, MODEL_VERSION, "model.joblib")

LOG_PATH = os.path.join(APP_ROOT, "predictions.log")
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup work
    global model, target_names
    try:
        model = load_model()
    except Exception as e:
        logging.error(f"Failed to load model: {e}")
        model = None
    target_names = ["setosa", "versicolor", "virginica"]
    yield
    # shutdown work (if needed)
    # e.g. close DB connections

app = FastAPI(title="ML Deployment Simulation", version="1.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = None
target_names = None


def load_model(path=MODEL_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model not found at {path}. Train and save a model first.")
    mdl = joblib.load(path)
    return mdl


class PredictResponse(BaseModel):
    # avoid pydantic protected namespace warning for 'model_'
    model_config = {"protected_namespaces": ()}

    prediction: str
    prediction_index: int
    probabilities: List[float]
    model_version: str


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded. Train the model or set MODEL_VERSION correctly.")

    features = req.features
    try:
        probs = model.predict_proba([features])[0].tolist()
        pred_idx = int(model.predict([features])[0])
        pred_label = target_names[pred_idx] if target_names else str(pred_idx)
    except Exception as e:
        logging.exception("Prediction error")
        raise HTTPException(status_code=400, detail=f"Prediction failed: {e}")

    payload = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "input": features,
        "prediction_index": pred_idx,
        "prediction_label": pred_label,
        "probabilities": probs,
        "model_version": MODEL_VERSION,
    }
    logging.info(payload)
    return {
        "prediction": pred_label,
        "prediction_index": pred_idx,
        "probabilities": probs,
        "model_version": MODEL_VERSION,
    }


# Feedback loop endpoint: accepts feature + optional true label to persist
class FeedbackIn(BaseModel):
    features: List[float]
    true_label: Optional[int] = None  # allow class index
    comment: Optional[str] = None


@app.post("/feedback")
def feedback(item: FeedbackIn):
    # Append feedback to a CSV file for manual inspection / future retraining
    feedback_dir = os.path.join(os.path.dirname(APP_ROOT), "data")
    os.makedirs(feedback_dir, exist_ok=True)
    fpath = os.path.join(feedback_dir, "feedback.csv")
    line = ",".join(map(str, item.features)) + "," + (str(item.true_label) if item.true_label is not None else "") + "," + (item.comment or "")
    with open(fpath, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    logging.info({"feedback": item.dict(), "model_version": MODEL_VERSION})
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)