import logging
import requests


class APIClient:
    """
    🇮🇹 Client HTTP riusabile per le chiamate API.
    🇬🇧 Reusable HTTP client for API calls.
    """

    def __init__(self, base_url, headers=None, timeout=5):
        """
        🇮🇹 Inizializza il client con URL di base e header opzionali.
        🇬🇧 Initialize client with base URL and optional headers.
        """
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {"Content-Type": "application/json"}
        self.timeout = timeout
        self.session = requests.Session()

        # Imposta logger
        self.log = logging.getLogger("APIClient")
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%H:%M:%S"
        )

    def get(self, endpoint, **kwargs):
        """
        🇮🇹 Esegue una richiesta GET.
        🇬🇧 Execute a GET request.
        """
        url = f"{self.base_url}{endpoint}"
        self.log.info(f"[GET] -> {url}")
        try:
            response = self.session.get(
                url,
                headers=self.headers,
                timeout=self.timeout,
                **kwargs
            )
            self._log_response(response)
            return response
        except requests.exceptions.RequestException as e:
            self.log.error(f"GET request failed: {e}")
            raise

    def post(self, endpoint, data=None, **kwargs):
        """
        🇮🇹 Esegue una richiesta POST con payload JSON.
        🇬🇧 Execute a POST request with JSON payload.
        """
        url = f"{self.base_url}{endpoint}"
        self.log.info(f"[POST] -> {url}")
        try:
            response = self.session.post(
                url,
                headers=self.headers,
                json=data,
                timeout=self.timeout,
                **kwargs
            )
            self._log_response(response)
            return response
        except requests.exceptions.RequestException as e:
            self.log.error(f"POST request failed: {e}")
            raise

    def _log_response(self, response):
        """
        🇮🇹 Logga lo stato e il messaggio di risposta.
        🇬🇧 Log the status and response message.
        """
        self.log.info(f"Response [{response.status_code}] -> {response.text[:150]}")
