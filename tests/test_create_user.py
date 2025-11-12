def test_create_user(api_client):
    """
    🇮🇹 Test di creazione utente su reqres.in
    🇬🇧 User creation test on reqres.in
    """
    payload = {"name": "Enrico", "job": "QA Manager"}
    response = api_client.post("/users", data=payload)

    assert response.status_code in (200, 201)
    print(response.json())
