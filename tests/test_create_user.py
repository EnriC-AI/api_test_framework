import pytest
import yaml
from pathlib import Path

@pytest.mark.parametrize("data", yaml.safe_load(open(Path(__file__).resolve().parent / "testdata" / "create_user_data.yaml")))
def test_create_user(api_client, data, logger):
    """
    🇮🇹 Esegue test di creazione utente con dati presi da file esterno YAML.
    🇬🇧 Executes user creation tests using data loaded from external YAML file.
    """
    logger.info(f"Creating user: {data['name']}")
    response = api_client.post("/users", json=data)
    assert response.status_code == 201
    logger.info(f"User created: {response.json()}")
