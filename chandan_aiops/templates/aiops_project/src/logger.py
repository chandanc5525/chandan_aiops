"""
Logging configuration
"""
import logging
import sys
from pathlib import Path
from config import Config

def setup_logging():
    """Setup logging configuration"""
    log_path = Path(Config.LOGS_PATH)
    log_path.mkdir(parents=True, exist_ok=True)
    
    log_file = log_path / "app.log"
    
    logging.basicConfig(
        level=getattr(logging, Config.LOG_LEVEL),
        format=Config.LOG_FORMAT,
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info("Logging setup completed")
    return logger