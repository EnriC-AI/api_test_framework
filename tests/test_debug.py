import requests

def test_direct_reqres_connection():
    """🇮🇹 Verifica se reqres.in risponde correttamente
       🇬🇧 Check if reqres.in responds correctly
    """
    resp = requests.get("https://reqres.in/api/users", headers={"x-api-key": "mock-key"})
    print("Status:", resp.status_code)
    print("Body:", resp.text[:100])
    assert resp.status_code == 200
