import csv
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TRAFFIC_CSV = os.path.join(BASE_DIR, "data", "raw", "traffic_data.csv")
DEFAULT_CITIES = ["Central", "North", "South", "East", "West"]


def generate_traffic_data_csv(csv_path: str = TRAFFIC_CSV, hours: int = 24, cities=None) -> str:
    cities = cities or DEFAULT_CITIES
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    header = ["location", "timestamp", "vehicle_count", "congestion_level"]
    start = datetime.now().replace(minute=0, second=0, microsecond=0) - timedelta(hours=hours - 1)

    rows = []
    for hour_offset in range(hours):
        timestamp = (start + timedelta(hours=hour_offset)).strftime("%Y-%m-%d %H:00")
        for city_index, city in enumerate(cities, start=1):
            base_count = 80 + city_index * 25
            noise = (hour_offset * 18 + city_index * 7) % 140
            vehicle_count = min(max(base_count + noise, 10), 520)

            if vehicle_count > 400:
                congestion_level = "High"
            elif vehicle_count > 220:
                congestion_level = "Medium"
            else:
                congestion_level = "Low"

            rows.append([city, timestamp, vehicle_count, congestion_level])

    with open(csv_path, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)

    return csv_path
