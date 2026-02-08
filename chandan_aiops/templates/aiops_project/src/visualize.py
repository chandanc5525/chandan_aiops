import subprocess
from pathlib import Path
from logger import setup_logger

logger = setup_logger()

def show_dvc_pipeline():
    dvc_file = Path("dvc.yaml")
    if not dvc_file.exists():
        logger.error("dvc.yaml not found. Please initialize a DVC pipeline first.")
        return

    logger.info("Generating DVC pipeline visualization...")
    try:
        # This command generates a pipeline graph in ASCII in terminal
        subprocess.run(["dvc", "pipeline", "show", "--ascii"], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to generate DVC pipeline: {e}")
