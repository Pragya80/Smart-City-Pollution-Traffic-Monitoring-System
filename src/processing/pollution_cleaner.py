import pandas as pd


def clean_dataframe(df):

    df = df.dropna(subset=["AQI"])

    df = df.reset_index(drop=True)

    return df


def standardize_datetime(df):

    if "Datetime" in df.columns:

        df["Datetime"] = pd.to_datetime(df["Datetime"])

    if "Date" in df.columns:

        df["Date"] = pd.to_datetime(df["Date"])

    return df


def categorize_aqi(aqi):

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Satisfactory"

    elif aqi <= 200:
        return "Moderate"

    elif aqi <= 300:
        return "Poor"

    elif aqi <= 400:
        return "Very Poor"

    else:
        return "Severe"


def add_aqi_category(df):

    df["AQI_Category"] = df["AQI"].apply(categorize_aqi)

    return df

def prepare_pollution_dataframe(df):

    df = clean_dataframe(df)

    df = standardize_datetime(df)

    df = add_aqi_category(df)

    return df