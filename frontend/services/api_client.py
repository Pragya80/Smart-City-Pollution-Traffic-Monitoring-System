from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import requests


@dataclass(frozen=True)
class ApiConfig:
    base_url: str
    use_mock: bool


def get_config() -> ApiConfig:
    base_url = os.getenv("BACKEND_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
    use_mock = os.getenv("USE_MOCK_API", "1") == "1"
    return ApiConfig(base_url=base_url, use_mock=use_mock)


def _mock(path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    params = params or {}
    city = params.get("city")

    if path == "/health":
        return {"status": "ok", "mock": True}
    if path == "/api/pollution/summary":
        return {"city": city, "count": 3, "avg_aqi": 253.3, "max_aqi": 310}
    if path == "/api/traffic/summary":
        return {"city": city, "count": 3, "avg_traffic_density": 85.0, "avg_speed": 18.0}
    if path == "/api/analytics/peak-hours":
        return {
            "city": city,
            "items": [
                {"hour": "08", "avg_traffic_density": 85.0},
                {"hour": "19", "avg_traffic_density": 92.0},
            ],
        }
    if path == "/api/analytics/high-risk-zones":
        return {
            "city": city,
            "items": [{"zone": "ITO", "avg_aqi": 310.0}, {"zone": "CP", "avg_aqi": 280.0}],
        }
    if path == "/api/analytics/correlation":
        return {"city": city, "aqi_vs_traffic_density": 0.72}

    return {"error": f"mock not implemented for {path}"}


def get(path: str, params: dict[str, Any] | None = None, timeout_s: int = 10) -> dict[str, Any]:
    cfg = get_config()
    if cfg.use_mock:
        return _mock(path, params=params)

    url = f"{cfg.base_url}{path}"
    resp = requests.get(url, params=params, timeout=timeout_s)
    resp.raise_for_status()
    return resp.json()

