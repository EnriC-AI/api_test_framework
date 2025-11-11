def test_smoke(api_client):
    """
    🇮🇹 Verifica base che il framework sia configurato correttamente.
    🇬🇧 Basic check to ensure the framework is correctly configured.
    """
    response = api_client.get("/users/1")
    assert response.status_code == 200
    assert "name" in response.json()
