from flask import Flask
from src.api.traffic_routes import traffic_bp
from src.database.sqlite_manager import create_table, insert_traffic_data_from_csv

app = Flask(__name__)

# Register traffic routes
app.register_blueprint(traffic_bp)

@app.route("/")
def index():
    return (
        "Smart City Pollution & Traffic Monitoring System API is running. "
        "Available endpoints: /traffic, /peak-hours"
    )


if __name__ == "__main__":
    # Step 1: Create table
    create_table()

    # Step 2: Load Kaggle dataset (city_hour.csv)
    insert_traffic_data_from_csv()

    # Step 3: Run server
    app.run(debug=True)