from locust import HttpUser, between, task


class APIUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def list_users(self):
        self.client.get("/api/users?page=1", name="GET /api/users?page=1")

    @task(1)
    def get_single_user(self):
        self.client.get("/api/users/2", name="GET /api/users/2")
