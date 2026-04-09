import pandas as pd

DATA_PATH = "data/raw/"


def load_city_day():
    return pd.read_csv(
        DATA_PATH + "city_day.csv",
        low_memory=False
    )


def load_city_hour():
    return pd.read_csv(
        DATA_PATH + "city_hour.csv",
        low_memory=False
    )


def load_station_day():
    return pd.read_csv(
        DATA_PATH + "station_day.csv",
        low_memory=False
    )


def load_station_hour():
    return pd.read_csv(
        DATA_PATH + "station_hour.csv",
        low_memory=False
    )


def load_stations():
    return pd.read_csv(
        DATA_PATH + "stations.csv",
        low_memory=False
    )


def load_all_pollution_data():

    return {
        "city_day": load_city_day(),
        "city_hour": load_city_hour(),
        "station_day": load_station_day(),
        "station_hour": load_station_hour(),
        "stations": load_stations()
    }