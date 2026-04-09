from flask import Blueprint, jsonify
from src.database.sqlite_manager import get_all_traffic, get_peak_hours

# THIS is what was missing ❗
traffic_bp = Blueprint("traffic", __name__)


@traffic_bp.route("/traffic", methods=["GET"])
def traffic():
    data = get_all_traffic()

    result = []
    for row in data:
        result.append({
            "location": row[0],
            "timestamp": row[1],
            "vehicle_count": row[2],
            "congestion_level": row[3]
        })

    return jsonify(result)


@traffic_bp.route("/peak-hours", methods=["GET"])
def peak_hours():
    data = get_peak_hours()

    result = []
    for row in data:
        result.append({
            "timestamp": row[0],
            "vehicle_count": row[1]
        })

    return jsonify(result)