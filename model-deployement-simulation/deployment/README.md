# ML Deployment Simulation - Usage

1) Install deps (recommended in venv):
   python -m pip install -r requirements.txt

2) Train model:
   cd model-deployement-simulation
   python train.py
   This creates models/v1/model.joblib

3) Run API locally:
   uvicorn api.app:app --reload

   Open docs: http://localhost:8000/docs

4) Test:
   python test_client.py

5) Docker:
   docker build -t ml-sim .
   docker run -p 8000:8000 -e MODEL_VERSION=v1 ml-sim

   Or with docker-compose:
   docker-compose up --build

Notes:
- Model versioning: models are stored under models/{version}/model.joblib. Change MODEL_VERSION env var to use a different model.
- Feedback: POST /feedback appends entries to data/feedback.csv for simulated live learning.
- Logs: API logs are written to api/predictions.log