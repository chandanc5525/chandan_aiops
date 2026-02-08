import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from logger import setup_logger, load_params

logger = setup_logger()
params = load_params()

processed_path = Path(params["data"]["processed_path"])
features_path = Path("data/processed/features.csv")
features_path.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(processed_path)

drop_cols = params["features"].get("drop_columns", [])
df = df.drop(columns=drop_cols, errors="ignore")

cat_encoding = params["features"].get("categorical_encoding", "onehot")
if cat_encoding == "onehot":
    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    df = pd.get_dummies(df, columns=cat_cols)

scaling = params["features"].get("scaling", "standard")
if scaling == "standard":
    num_cols = df.select_dtypes(include=["float64", "int64"]).columns
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

df.to_csv(features_path, index=False)
logger.info(f"Feature preprocessing completed and saved to {features_path}")
