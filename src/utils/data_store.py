from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd


@dataclass(frozen=True)
class DataPaths:
    processed_csv: Path


DEFAULT_PATHS = DataPaths(
    processed_csv=Path("data/processed/final_merged_data.csv"),
)


_CACHE: dict[str, pd.DataFrame] = {}


def load_processed_df(paths: DataPaths = DEFAULT_PATHS) -> pd.DataFrame:
    """
    Loads the merged dataset if present, otherwise returns a tiny demo dataset.
    """
    cache_key = str(paths.processed_csv)
    if cache_key in _CACHE:
        return _CACHE[cache_key]

    if paths.processed_csv.exists():
        df = pd.read_csv(paths.processed_csv)
        _CACHE[cache_key] = df
        return df

    demo = pd.DataFrame(
        [
            {
                "city": "Delhi",
                "datetime": "2020-01-01 08:00:00",
                "aqi": 280,
                "pm25": 160,
                "pm10": 240,
                "traffic_density": 85,
                "vehicle_count": 1200,
                "avg_speed": 18,
                "zone": "CP",
            },
            {
                "city": "Delhi",
                "datetime": "2020-01-01 19:00:00",
                "aqi": 310,
                "pm25": 190,
                "pm10": 270,
                "traffic_density": 92,
                "vehicle_count": 1500,
                "avg_speed": 14,
                "zone": "ITO",
            },
            {
                "city": "Mumbai",
                "datetime": "2020-01-01 09:00:00",
                "aqi": 170,
                "pm25": 95,
                "pm10": 140,
                "traffic_density": 78,
                "vehicle_count": 980,
                "avg_speed": 22,
                "zone": "BKC",
            },
        ]
    )
    _CACHE[cache_key] = demo
    return demo


def to_records(df: pd.DataFrame, limit: int = 500) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    return df.head(limit).to_dict(orient="records")

