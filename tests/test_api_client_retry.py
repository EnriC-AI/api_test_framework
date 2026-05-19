from unittest.mock import MagicMock

from core.api_client import APIClient


def test_api_client_mounts_retry_adapter():
    client = APIClient("https://example.com", retries=2)
    https_adapter = client.session.get_adapter("https://")
    assert https_adapter.max_retries.total == 2


def test_api_client_injects_correlation_header(monkeypatch):
    client = APIClient("https://example.com")

    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.text = '{"ok": true}'

    captured = {}

    def fake_request(method, url, **kwargs):
        captured["method"] = method
        captured["url"] = url
        captured["headers"] = kwargs["headers"]
        return fake_response

    monkeypatch.setattr(client.session, "request", fake_request)

    response = client.get("/health", correlation_id="test-correlation-id")

    assert response.status_code == 200
    assert captured["method"] == "GET"
    assert captured["url"] == "https://example.com/health"
    assert captured["headers"]["X-Correlation-ID"] == "test-correlation-id"
