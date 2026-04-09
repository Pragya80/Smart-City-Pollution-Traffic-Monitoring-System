from src.ingestion.pollution_pipeline import get_pollution_data


def test_pipeline():

    print("\nRunning Pollution Pipeline Test...\n")

    data = get_pollution_data()

    print("Pipeline executed successfully\n")

    print("Available datasets:")
    print(list(data.keys()))

    print("\nCity Data Sample:\n")
    print(data["city_data"].head())

    print("\nTotal Rows:")
    print(len(data["city_data"]))

    print("\nColumns:")
    print(list(data["city_data"].columns))

    print("\nPipeline working correctly")


if __name__ == "__main__":
    test_pipeline()