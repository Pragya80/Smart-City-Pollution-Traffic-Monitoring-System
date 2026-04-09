from src.ingestion.pollution_loader import load_all_pollution_data
from src.processing.data_merger import build_pollution_dataset


def get_pollution_data():
    """
    Main entry point for the pollution data pipeline.
    Loads raw data and returns processed datasets.
    """

    # Load raw datasets
    raw_data = load_all_pollution_data()

    # Build processed datasets
    processed_data = build_pollution_dataset(raw_data)

    return processed_data