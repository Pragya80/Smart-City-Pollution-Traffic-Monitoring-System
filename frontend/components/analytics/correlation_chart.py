import streamlit as st


def render_correlation_chart(payload: dict):
    st.subheader("AQI vs Traffic correlation")
    corr = payload.get("aqi_vs_traffic_density")
    if corr is None:
        st.info("No correlation available.")
        return

    st.metric("Pearson correlation", round(float(corr), 3))

