import pandas as pd
import pickle
from logger import setup_logger, load_params
from pathlib import Path

logger = setup_logger()
params = load_params()

input_path = Path(params["prediction"]["input_path"])
output_path = Path(params["prediction"]["output_path"])
output_path.parent.mkdir(parents=True, exist_ok=True)

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

df = pd.read_csv(input_path)
predictions = model.predict(df)
df["prediction"] = predictions
df.to_csv(output_path, index=False)

logger.info(f"Predictions saved to {output_path}")
