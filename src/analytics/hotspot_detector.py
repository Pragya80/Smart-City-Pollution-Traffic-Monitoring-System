# src/analytics/hotspot_detector.py
import pandas as pd


class HotspotDetector:
    def __init__(self, station_hour_path: str):
        self.station_hour = pd.read_csv(station_hour_path)

    def top_polluted_stations(self, top_n=10):
        result = (
            self.station_hour.groupby("StationId")["AQI"]
            .mean()
            .sort_values(ascending=False)
            .head(top_n)
            .reset_index()
        )
        return result.to_dict(orient="records")

    def red_zone_stations(self, threshold=300):
        red_zones = self.station_hour[self.station_hour["AQI"] >= threshold]
        return red_zones[["StationId", "AQI"]].to_dict(orient="records")