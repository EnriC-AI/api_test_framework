import json
from pathlib import Path

import pytest
from jsonschema import validate


@pytest.mark.contract
def test_get_single_user_contract(api_client):
    """Validate OpenAPI contract excerpt for GET /users/{id}."""
    contract_path = Path(__file__).resolve().parent / "contracts" / "reqres_openapi_excerpt.json"
    with open(contract_path, encoding="utf-8") as f:
        contract = json.load(f)

    response = api_client.get("/users/2")
    assert response.status_code == 200

    schema = contract["components"]["schemas"]["GetSingleUserResponse"]
    validate(instance=response.json(), schema=schema)
