import pandas as pd
import plotly.express as px
import streamlit as st


def render_peak_hours_chart(payload: dict):
    st.subheader("Peak traffic hours")
    items = payload.get("items") or []
    if not items:
        st.info("No peak hour data available.")
        return

    df = pd.DataFrame(items)
    fig = px.bar(df, x="hour", y="avg_traffic_density", title="Avg traffic density by hour")
    st.plotly_chart(fig, use_container_width=True)

