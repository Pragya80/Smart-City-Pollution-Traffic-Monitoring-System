from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Query

from src.utils.data_store import load_processed_df

router = APIRouter()


@router.get("/peak-hours")
def peak_hours(city: str | None = Query(default=None)) -> dict[str, Any]:
    df = load_processed_df()
    if city:
        df = df[df.get("city").astype(str).str.lower() == city.lower()]

    if df.empty or "datetime" not in df.columns or "traffic_density" not in df.columns:
        return {"city": city, "items": []}

    dfx = df.copy()
    dfx["datetime"] = dfx["datetime"].astype(str)
    dfx["hour"] = dfx["datetime"].str[11:13]
    grouped = (
        dfx.groupby("hour", dropna=True)["traffic_density"]
        .mean()
        .sort_values(ascending=False)
        .head(6)
    )
    items = [{"hour": str(hour), "avg_traffic_density": float(val)} for hour, val in grouped.items()]
    return {"city": city, "items": items}


@router.get("/correlation")
def correlation(city: str | None = Query(default=None)) -> dict[str, Any]:
    df = load_processed_df()
    if city:
        df = df[df.get("city").astype(str).str.lower() == city.lower()]

    if df.empty or "aqi" not in df.columns or "traffic_density" not in df.columns:
        return {"city": city, "aqi_vs_traffic_density": None}

    corr = df["aqi"].corr(df["traffic_density"])
    return {"city": city, "aqi_vs_traffic_density": None if corr is None else float(corr)}


@router.get("/high-risk-zones")
def high_risk_zones(city: str | None = Query(default=None), limit: int = Query(default=10, ge=1, le=100)) -> dict[str, Any]:
    df = load_processed_df()
    if city:
        df = df[df.get("city").astype(str).str.lower() == city.lower()]

    if df.empty or "zone" not in df.columns or "aqi" not in df.columns:
        return {"city": city, "items": []}

    grouped = df.groupby("zone", dropna=True)["aqi"].mean().sort_values(ascending=False).head(limit)
    items = [{"zone": str(zone), "avg_aqi": float(val)} for zone, val in grouped.items()]
    return {"city": city, "items": items}

