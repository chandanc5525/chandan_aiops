import logging
from pathlib import Path
import yaml

def setup_logger(log_dir: str = "logs", level: str = "INFO"):
    Path(log_dir).mkdir(exist_ok=True, parents=True)
    logger = logging.getLogger("AIOps")
    logger.setLevel(level)
    fh = logging.FileHandler(Path(log_dir) / "pipeline.log")
    ch = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

def load_params(path: str = "params.yaml"):
    import yaml
    with open(path, "r") as f:
        params = yaml.safe_load(f)
    return params
