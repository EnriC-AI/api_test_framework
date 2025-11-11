def test_create_user(api_client):
    """
    🇮🇹 Test fittizio per POST. L'API non salva veramente, ma risponde qualcosa.
    🇬🇧 Fake POST test. API doesn't save but returns something.
    """
    payload = {
        "name": "Mario Rossi",
        "email": "mario.rossi@example.com"
    }

    response = api_client.post("/users", data=payload)

    assert response.status_code in (200, 201)
    assert response.json()["name"] == "Mario Rossi"
