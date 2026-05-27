import os

import requests



def test_direct_reqres_connection():
    """🇮🇹 Verifica se reqres.in risponde correttamente
       🇬🇧 Check if reqres.in responds correctly
    """
    headers = {}
    api_key = os.getenv("REQRES_API_KEY")
    if api_key:
        headers["x-api-key"] = api_key

    resp = requests.get("https://reqres.in/api/users", headers=headers)
    print("Status:", resp.status_code)
    print("Body:", resp.text[:100])
    assert resp.status_code == 200
