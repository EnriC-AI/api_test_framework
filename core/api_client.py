import logging
import requests


class APIClient:
    """
    🇮🇹 Semplice client HTTP riusabile.
    🇬🇧 Simple reusable HTTP client.
    """

    def __init__(self, base_url, timeout=5):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

        self.log = logging.getLogger("APIClient")
        logging.basicConfig(level=logging.INFO)

    def get(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self.log.info(f"[GET] -> {url}")
        response = self.session.get(url, timeout=self.timeout, **kwargs)
        return response

    def post(self, endpoint, data=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self.log.info(f"[POST] -> {url}")
        response = self.session.post(url, json=data, timeout=self.timeout, **kwargs)
        return response
