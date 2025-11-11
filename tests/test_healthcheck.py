def test_healthcheck(api_client):
    """
    🇮🇹 Verifica che l'API risponda correttamente.
    🇬🇧 Verifies that the API responds correctly.
    """
    response = api_client.get("/users")
    assert response.status_code == 200
