# src/analytics/pollution_analysis.py
import pandas as pd


class PollutionAnalysis:
    def __init__(self, city_day_path: str, city_hour_path: str):
        self.city_day = pd.read_csv(city_day_path)
        self.city_hour = pd.read_csv(city_hour_path)

    def top_polluted_cities(self, top_n=10):
        df = self.city_day.groupby("City")["AQI"].mean().reset_index()
        df = df.sort_values("AQI", ascending=False).head(top_n)
        return df.to_dict(orient="records")

    def peak_pollution_hours(self):
        self.city_hour["Datetime"] = pd.to_datetime(self.city_hour["Datetime"])
        self.city_hour["hour"] = self.city_hour["Datetime"].dt.hour

        result = (
            self.city_hour.groupby("hour")["AQI"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )
        return result.to_dict(orient="records")