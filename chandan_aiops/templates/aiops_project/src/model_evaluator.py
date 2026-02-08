import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from logger import setup_logger, load_params
from pathlib import Path
import json

logger = setup_logger()
params = load_params()

features_path = Path("data/processed/features.csv")
model_path = Path("models/model.pkl")
metrics_path = Path("reports/metrics.json")
metrics_path.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(features_path)
target_col = params["data"]["target_column"]

X = df.drop(columns=[target_col])
y = df[target_col]

with open(model_path, "rb") as f:
    model = pickle.load(f)

y_pred = model.predict(X)

metrics = {
    "accuracy": accuracy_score(y, y_pred),
    "precision": precision_score(y, y_pred, zero_division=0),
    "recall": recall_score(y, y_pred, zero_division=0),
    "f1": f1_score(y, y_pred, zero_division=0)
}

with open(metrics_path, "w") as f:
    json.dump(metrics, f, indent=4)

logger.info(f"Model evaluation completed. Metrics saved to {metrics_path}")
