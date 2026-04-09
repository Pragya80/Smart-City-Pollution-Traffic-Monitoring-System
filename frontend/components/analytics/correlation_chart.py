# frontend/components/analytics/correlation_chart.py
import streamlit as st
import pandas as pd
import plotly.express as px


def render_correlation_chart(df: pd.DataFrame):
    fig = px.scatter(
        df,
        x="traffic_density",
        y="AQI",
        color="city",
        title="AQI vs Traffic Density"
    )
    st.plotly_chart(fig, use_container_width=True)