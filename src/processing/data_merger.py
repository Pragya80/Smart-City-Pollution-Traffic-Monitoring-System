def merge_station_data(station_day, stations):

    merged_df = station_day.merge(
        stations,
        on="StationId",
        how="left"
    )

    return merged_df


def create_unified_dataset(data):

    city_day = data["city_day"]

    station_day = data["station_day"]

    stations = data["stations"]

    merged_station = merge_station_data(
        station_day,
        stations
    )

    return {
        "city": city_day,
        "station": merged_station
    }
from src.processing.pollution_cleaner import (
    prepare_pollution_dataframe
)


def build_pollution_dataset(data):

    city_df = prepare_pollution_dataframe(
        data["city_day"]
    )

    station_df = prepare_pollution_dataframe(
        data["station_day"]
    )

    stations = data["stations"]

    merged_station = station_df.merge(
        stations,
        on="StationId",
        how="left"
    )

    return {
        "city_data": city_df,
        "station_data": merged_station
    }