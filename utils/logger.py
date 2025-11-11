import logging
from datetime import datetime
import os

def get_logger():
    """
    🇮🇹 Crea un logger centralizzato che scrive su file e console.
    🇬🇧 Creates a centralized logger that writes to both file and console.
    """
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)  # 🇮🇹 Crea la cartella logs se non esiste / 🇬🇧 Create logs folder if missing
    log_file = os.path.join(log_dir, f"test_{datetime.now().strftime('%Y%m%d')}.log")

    logger = logging.getLogger("api_logger")

    # 🇮🇹 Evita di aggiungere più handler se già configurato
    # 🇬🇧 Avoid adding multiple handlers if already configured
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(log_file)
        ch = logging.StreamHandler()

        # 🇮🇹 Formato leggibile per timestamp, livello e messaggio
        # 🇬🇧 Readable format for timestamp, level, and message
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
