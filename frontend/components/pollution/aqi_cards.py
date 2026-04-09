import streamlit as st


def render_aqi_cards(summary: dict):
    st.subheader("Pollution")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Records", summary.get("count"))
    with col2:
        st.metric("Avg AQI", summary.get("avg_aqi"))
    with col3:
        st.metric("Max AQI", summary.get("max_aqi"))

