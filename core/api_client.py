import logging
import time
import uuid

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class APIClient:
    """
    🇮🇹 Client HTTP riusabile per le chiamate API.
    🇬🇧 Reusable HTTP client for API calls.
    """

    def __init__(
        self,
        base_url,
        headers=None,
        timeout=5,
        retries=3,
        backoff_factor=0.5,
        retry_statuses=(429, 500, 502, 503, 504),
    ):
        """
        🇮🇹 Inizializza il client con URL di base e header opzionali.
        🇬🇧 Initialize client with base URL and optional headers.
        """
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {"Content-Type": "application/json"}
        self.timeout = timeout
        self.session = requests.Session()

        retry_strategy = Retry(
            total=retries,
            connect=retries,
            read=retries,
            status=retries,
            allowed_methods=frozenset(["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"]),
            status_forcelist=retry_statuses,
            backoff_factor=backoff_factor,
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        self.log = logging.getLogger("APIClient")
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%H:%M:%S",
        )

    def get(self, endpoint, **kwargs):
        """
        🇮🇹 Esegue una richiesta GET.
        🇬🇧 Execute a GET request.
        """
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, data=None, **kwargs):
        """
        🇮🇹 Esegue una richiesta POST con payload JSON.
        🇬🇧 Execute a POST request with JSON payload.
        """
        return self._request("POST", endpoint, json=data, **kwargs)

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        correlation_id = kwargs.pop("correlation_id", str(uuid.uuid4()))
        request_headers = kwargs.pop("headers", {})
        merged_headers = {**self.headers, **request_headers, "X-Correlation-ID": correlation_id}

        self.log.info(f"[{method}] -> {url} | correlation_id={correlation_id}")

        start = time.perf_counter()
        try:
            response = self.session.request(
                method,
                url,
                headers=merged_headers,
                timeout=self.timeout,
                **kwargs,
            )
        except requests.exceptions.RequestException as e:
            elapsed_ms = (time.perf_counter() - start) * 1000
            self.log.error(
                f"[{method}] xx {url} | correlation_id={correlation_id} | elapsed_ms={elapsed_ms:.2f} | error={e}"
            )
            raise

        elapsed_ms = (time.perf_counter() - start) * 1000
        self._log_response(response, method, url, correlation_id, elapsed_ms)
        return response

    def _log_response(self, response, method, url, correlation_id, elapsed_ms):
        """
        🇮🇹 Logga stato e timing della risposta.
        🇬🇧 Log response status and timing.
        """
        body_preview = response.text[:150].replace("\n", " ")
        self.log.info(
            f"[{method}] <- {response.status_code} {url} | correlation_id={correlation_id} | "
            f"elapsed_ms={elapsed_ms:.2f} | body={body_preview}"
        )
