import logging
from datetime import datetime
from pathlib import Path

# 🇮🇹 Imposta un logger personalizzato per l'intero framework.
# 🇬🇧 Set up a custom logger for the entire framework.

def get_logger(name="api_framework"):
    # 🇮🇹 Crea la cartella "logs" se non esiste
    # 🇬🇧 Create "logs" folder if it doesn't exist
    log_dir = Path(__file__).resolve().parent / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    # 🇮🇹 Nome file log basato su data/ora
    # 🇬🇧 Log file name based on current date/time
    log_file = log_dir / f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 🇮🇹 Evita duplicazione handler
    # 🇬🇧 Avoid duplicate handlers
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
