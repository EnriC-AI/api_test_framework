import pytest
import yaml
from pathlib import Path
from core.logs.logger import get_logger
from core.api_client import APIClient

@pytest.fixture(scope="session")
def config():
    """
    🇮🇹 Carica la configurazione in base all'ambiente selezionato.
    🇬🇧 Load configuration depending on selected environment.
    """
    base_path = Path(__file__).resolve().parent
    with open(base_path / "config/config.yaml") as f:
        full_config = yaml.safe_load(f)

    env = full_config.get("default_env", "dev")
    return full_config["environments"][env]


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
