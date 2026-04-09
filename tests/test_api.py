from fastapi.testclient import TestClient

from app import app


def test_health_ok():
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_analytics_peak_hours_contract():
    client = TestClient(app)
    resp = client.get("/api/analytics/peak-hours")
    assert resp.status_code == 200
    body = resp.json()
    assert "items" in body
    assert isinstance(body["items"], list)

