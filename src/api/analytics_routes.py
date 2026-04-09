# src/api/analytics_routes.py
from fastapi import APIRouter
from src.analytics.pollution_analysis import PollutionAnalysis
from src.analytics.hotspot_detector import HotspotDetector
from src.analytics.correlation_engine import CorrelationEngine

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/top-polluted-cities")
def top_polluted_cities():
    engine = PollutionAnalysis(
        "data/raw/city_day.csv",
        "data/raw/city_hour.csv"
    )
    return engine.top_polluted_cities()


@router.get("/peak-pollution-hours")
def peak_hours():
    engine = PollutionAnalysis(
        "data/raw/city_day.csv",
        "data/raw/city_hour.csv"
    )
    return engine.peak_pollution_hours()


@router.get("/top-polluted-stations")
def top_stations():
    detector = HotspotDetector("data/raw/station_hour.csv")
    return detector.top_polluted_stations()


@router.get("/red-zone-stations")
def red_zones():
    detector = HotspotDetector("data/raw/station_hour.csv")
    return detector.red_zone_stations()