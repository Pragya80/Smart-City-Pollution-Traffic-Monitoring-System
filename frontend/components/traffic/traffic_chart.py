import requests
import matplotlib.pyplot as plt

def plot_traffic():
    response = requests.get("http://127.0.0.1:5000/traffic")
    data = response.json()

    aggregated = {}
    for item in data:
        aggregated[item["timestamp"]] = aggregated.get(item["timestamp"], 0) + item["vehicle_count"]

    timestamps = sorted(aggregated.keys())
    vehicle_counts = [aggregated[t] for t in timestamps]

    plt.figure()
    plt.plot(timestamps, vehicle_counts, marker="o")
    plt.xlabel("Time")
    plt.ylabel("Total Vehicle Count")
    plt.title("Traffic Density")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()