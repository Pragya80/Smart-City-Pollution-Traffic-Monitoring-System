from __future__ import annotations

from fastapi import APIRouter, Query

from src.utils.data_store import load_processed_df, to_records

router = APIRouter()


@router.get("/summary")
def traffic_summary(city: str | None = Query(default=None)):
    df = load_processed_df()
    if city:
        df = df[df.get("city").astype(str).str.lower() == city.lower()]

    if df.empty:
        return {"city": city, "count": 0, "avg_traffic_density": None, "avg_speed": None}

    density = df["traffic_density"] if "traffic_density" in df.columns else None
    speed = df["avg_speed"] if "avg_speed" in df.columns else None
    return {
        "city": city,
        "count": int(len(df)),
        "avg_traffic_density": float(density.mean()) if density is not None else None,
        "avg_speed": float(speed.mean()) if speed is not None else None,
    }


@router.get("/records")
def traffic_records(city: str | None = Query(default=None), limit: int = Query(default=200, ge=1, le=2000)):
    df = load_processed_df()
    if city:
        df = df[df.get("city").astype(str).str.lower() == city.lower()]
    return {"items": to_records(df, limit=limit)}

