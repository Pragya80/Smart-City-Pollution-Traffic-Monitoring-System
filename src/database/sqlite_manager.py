import os
import sqlite3
import pandas as pd
from src.ingestion.traffic_loader import generate_traffic_data_csv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DB_PATH = os.path.join(BASE_DIR, "database", "smart_city.db")
CSV_PATH = os.path.join(BASE_DIR, "data", "raw", "traffic_data.csv")


def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS traffic (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT,
        timestamp TEXT,
        vehicle_count INTEGER,
        congestion_level TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_traffic_data_from_csv():
    if not os.path.exists(CSV_PATH) or os.path.getsize(CSV_PATH) == 0:
        generate_traffic_data_csv(CSV_PATH)

    df = pd.read_csv(CSV_PATH)
    df = df.dropna(subset=["location", "timestamp", "vehicle_count"])

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM traffic")

    for _, row in df.iterrows():
        cursor.execute("""
        INSERT INTO traffic (location, timestamp, vehicle_count, congestion_level)
        VALUES (?, ?, ?, ?)
        """, (
            row["location"],
            row["timestamp"],
            int(row["vehicle_count"]),
            row.get("congestion_level", "Low")
        ))

    conn.commit()
    conn.close()


# ✅ THIS WAS MISSING
def get_all_traffic():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT location, timestamp, vehicle_count, congestion_level FROM traffic ORDER BY timestamp"
    )
    rows = cursor.fetchall()

    conn.close()
    return rows


# ✅ THIS WAS MISSING
def get_peak_hours():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT timestamp, MAX(vehicle_count)
    FROM traffic
    GROUP BY timestamp
    ORDER BY MAX(vehicle_count) DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows