from __future__ import annotations

from fastapi import APIRouter, Query

from src.utils.data_store import load_processed_df, to_records

router = APIRouter()


@router.get("/summary")
def pollution_summary(city: str | None = Query(default=None)):
    df = load_processed_df()
    if city:
        df = df[df.get("city").astype(str).str.lower() == city.lower()]

    if df.empty:
        return {"city": city, "count": 0, "avg_aqi": None, "max_aqi": None}

    aqi = df["aqi"] if "aqi" in df.columns else None
    return {
        "city": city,
        "count": int(len(df)),
        "avg_aqi": float(aqi.mean()) if aqi is not None else None,
        "max_aqi": float(aqi.max()) if aqi is not None else None,
    }


@router.get("/records")
def pollution_records(city: str | None = Query(default=None), limit: int = Query(default=200, ge=1, le=2000)):
    df = load_processed_df()
    if city:
        df = df[df.get("city").astype(str).str.lower() == city.lower()]
    return {"items": to_records(df, limit=limit)}

