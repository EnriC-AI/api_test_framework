import json
import pytest
from pathlib import Path


@pytest.mark.parametrize("data", json.loads(
    Path("tests/testdata/users_test_data.json").read_text()
))
def test_get_user_parametrized(api_client, data):
    """
    🇮🇹 Test parametrico basato su file JSON.
    🇬🇧 Parametric test powered by JSON file.
    """
    user_id = data["user_id"]
    expected_name = data["expected_name"]

    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["name"] == expected_name
