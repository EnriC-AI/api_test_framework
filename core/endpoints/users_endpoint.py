"""
🇮🇹 Endpoint dedicato agli utenti: incapsula le chiamate API relative al dominio 'users'.
🇬🇧 Dedicated endpoint for users: encapsulates all API calls related to the 'users' domain.
"""

class UsersEndpoint:
    def __init__(self, client):
        # 🇮🇹 APIClient passato come dipendenza (Dependency Injection)
        # 🇬🇧 APIClient passed as a dependency (Dependency Injection)
        self.client = client

    def get_user(self, user_id):
        # 🇮🇹 Richiede i dettagli di un utente tramite ID
        # 🇬🇧 Requests user details by ID
        return self.client.get(f"/users/{user_id}")

    def create_user(self, payload):
        # 🇮🇹 Crea un nuovo utente inviando un payload JSON
        # 🇬🇧 Creates a new user using a JSON payload
        return self.client.post("/users", data=payload)
