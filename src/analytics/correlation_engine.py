# src/analytics/correlation_engine.py
import pandas as pd


class CorrelationEngine:
    def __init__(self, merged_data_path: str):
        self.df = pd.read_csv(merged_data_path)

    def traffic_aqi_correlation(self):
        corr = self.df["AQI"].corr(self.df["traffic_density"])
        return {"aqi_traffic_correlation": round(float(corr), 4)}