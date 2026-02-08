import pandas as pd
from pathlib import Path
from logger import setup_logger, load_params

logger = setup_logger()
params = load_params()

raw_path = Path(params["data"]["raw_path"])
processed_path = Path(params["data"]["processed_path"])
processed_path.parent.mkdir(parents=True, exist_ok=True)

logger.info(f"Reading raw data from {raw_path}")
df = pd.read_csv(raw_path)

logger.info(f"Writing processed data to {processed_path}")
df.to_csv(processed_path, index=False)
logger.info("Data ingestion completed successfully.")
