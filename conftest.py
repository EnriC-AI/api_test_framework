import pytest
import yaml
from pathlib import Path
from core.logs.logger import get_logger
from core.api_client import APIClient


def pytest_addoption(parser):
    """
    🇮🇹 Aggiunge il flag CLI --env per selezionare l'ambiente.
    🇬🇧 Add --env CLI flag to select test environment.
    """
    parser.addoption(
        "--env",
        action="store",
        default=None,
        help="Target environment name from config/config.yaml (e.g. dev, mock, prod).",
    )


@pytest.fixture(scope="session")
def config(request):
    """
    🇮🇹 Carica la configurazione in base all'ambiente selezionato.
    🇬🇧 Load configuration depending on selected environment.
    """
    base_path = Path(__file__).resolve().parent
    with open(base_path / "config/config.yaml") as f:
        full_config = yaml.safe_load(f)

    selected_env = request.config.getoption("--env")
    env = selected_env or full_config.get("default_env", "dev")
    environments = full_config.get("environments", {})

    if env not in environments:
        available_envs = ", ".join(sorted(environments.keys()))
        raise pytest.UsageError(
            f"Unknown environment '{env}'. Available environments: {available_envs}"
        )

    return environments[env]


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
    headers = {"Content-Type": "application/json", "x-api-key": config.get("api_key", "")}
    client = APIClient(base_url, headers=headers)
    logger.info(f"API Client initialized with base URL: {base_url}")
    return client


@pytest.fixture(scope="session")
def user_schema():
    """
    🇮🇹 Espone il path dello schema utente ai test.
    🇬🇧 Expose user schema path to tests.
    """
    return Path(__file__).resolve().parent / "tests" / "schemas" / "user_schema.json"
