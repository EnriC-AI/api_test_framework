from pathlib import Path
import yaml
import json
import pytest
from core.api_client import APIClient



@pytest.fixture(scope="session")
def config():
    """
    🇮🇹 Carica i file di configurazione usando percorsi assoluti.
    🇬🇧 Load configuration files using absolute paths.
    """
    base_path = Path(__file__).resolve().parent

    # Se conftest è in tests/, risali di 1 livello
    if (base_path / "config").exists() is False:
        base_path = base_path.parent

    with open(base_path / "config/config.yaml") as f:
        main_conf = yaml.safe_load(f)

    env_name = main_conf["default"]
    env_path = base_path / main_conf["environments"][env_name]

    with open(env_path) as f:
        env_conf = yaml.safe_load(f)

    return env_conf


@pytest.fixture(scope="session")
def api_client(config):
    """
    🇮🇹 Istanzia l'API client con i parametri caricati da config.
    🇬🇧 Instantiate the API client using config parameters.
    """
    return APIClient(
        base_url=config["base_url"],
        timeout=config.get("timeout", 5)
    )


@pytest.fixture(scope="session")
def user_schema():
    """
    🇮🇹 Carica lo schema JSON degli utenti.
    🇬🇧 Load user JSON schema.
    """
    base_path = Path(__file__).resolve().parent.parent
    schema_path = base_path / "tests/schemas/user_schema.json"

    with open(schema_path) as f:
        return json.load(f)

# @pytest.fixture(scope="session")
# def config():
#     """
#     🇮🇹 Carica config.yaml in modo affidabile indipendentemente dalla posizione di esecuzione.
#     🇬🇧 Load config.yaml in a reliable way regardless of execution location.
#     """
#     base_path = Path(__file__).resolve().parent.parent
#
#     config_path = base_path / "config" / "config.yaml"
#
#     if not config_path.exists():
#         raise FileNotFoundError(f"Config file not found at: {config_path}")
#
#     with open(config_path, "r") as f:
#         return yaml.safe_load(f)

