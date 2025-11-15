import logging
import requests


class APIClient:
    """
    🇮🇹 Client HTTP riusabile per i test API.
    🇬🇧 Reusable HTTP client for API testing.
    """

    def __init__(self, base_url, headers=None, timeout=5):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

        self.log = logging.getLogger("APIClient")
        logging.basicConfig(level=logging.INFO)

    def get(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self.log.info(f"[GET] -> {url}")
        response = self.session.get(url, timeout=self.timeout, **kwargs)
        self.log.info(f"[GET] <- {response.status_code}")
        return response

    def post(self, endpoint, data=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self.log.info(f"[POST] -> {url} | Payload: {data}")
        response = self.session.post(url, json=data, timeout=self.timeout, **kwargs)
        self.log.info(f"[POST] <- {response.status_code} | Body: {response.text}")
        return response
