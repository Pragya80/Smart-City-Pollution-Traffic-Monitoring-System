import streamlit as st


def show_aqi_cards(df):

    avg_aqi = int(df["AQI"].mean())

    max_aqi = int(df["AQI"].max())

    min_aqi = int(df["AQI"].min())

    col1, col2, col3 = st.columns(3)

    col1.metric(
        label="Average AQI",
        value=avg_aqi
    )

    col2.metric(
        label="Max AQI",
        value=max_aqi
    )

    col3.metric(
        label="Min AQI",
        value=min_aqi
    )