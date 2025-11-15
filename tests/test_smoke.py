def test_smoke(api_client):
    """
    🇮🇹 Smoke test rapido per confermare che l'API risponda.
    🇬🇧 Quick smoke test to confirm API availability.
    """
    response = api_client.get("/users")
    assert response.status_code == 200
