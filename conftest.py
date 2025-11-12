import pytest
import yaml
from pathlib import Path
from core.logs.logger import get_logger
from core.api_client import APIClient

@pytest.fixture(scope="session")
def config():
    """
    🇮🇹 Carica i file di configurazione YAML.
    🇬🇧 Load YAML configuration files.
    """
    base_path = Path(__file__).resolve().parent
    with open(base_path / "config/config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def logger():
    """
    🇮🇹 Fornisce un logger globale ai test.
    🇬🇧 Provide a global logger to all tests.
    """
    return get_logger()

@pytest.fixture(scope="session")
def api_client(config, logger):
    """
    🇮🇹 Crea un'istanza di APIClient condivisa.
    🇬🇧 Create a shared instance of APIClient.
    """
    base_url = config["base_url"]
    client = APIClient(base_url)
    logger.info(f"API Client initialized with base URL: {base_url}")
    return client
