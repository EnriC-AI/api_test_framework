import pytest
from core.utils.validation import validate_json_schema
from pathlib import Path

@pytest.mark.parametrize("user_id", [1, 2])
def test_get_user_schema(api_client, user_schema, user_id, logger):
    """
    🇮🇹 Verifica che la risposta dell'endpoint rispetti lo schema JSON definito.
    🇬🇧 Validate that the API response matches the defined JSON schema.
    """
    response = api_client.get(f"/users/{user_id}")
    assert response.status_code == 200
    response_json = response.json()

    # Path allo schema
    schema_path = Path(__file__).resolve().parent / "schemas" / "user_schema.json"

    valid, error = validate_json_schema(response_json, schema_path)
    if not valid:
        logger.error(f"Schema validation failed: {error}")
    assert valid, f"Schema validation failed: {error}"
