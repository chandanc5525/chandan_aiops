import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from logger import setup_logger, load_params
from pathlib import Path

logger = setup_logger()
params = load_params()

features_path = Path("data/processed/features.csv")
model_path = Path("models/model.pkl")
model_path.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(features_path)
target_col = params["data"]["target_column"]

X = df.drop(columns=[target_col])
y = df[target_col]

split_params = params.get("split", {})
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=split_params.get("test_size", 0.2),
    shuffle=split_params.get("shuffle", True),
    random_state=params.get("project", {}).get("random_state", 42)
)

model_params = params.get("model", {}).get("params", {})
model = RandomForestClassifier(**model_params)
model.fit(X_train, y_train)

with open(model_path, "wb") as f:
    pickle.dump(model, f)

logger.info(f"Model trained and saved to {model_path}")
