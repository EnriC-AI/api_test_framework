def test_healthcheck(api_client):
    """
    🇮🇹 Controlla che l'endpoint sia raggiungibile.
    🇬🇧 Checks that the endpoint is reachable.
    """
    response = api_client.get("/users?page=1")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
