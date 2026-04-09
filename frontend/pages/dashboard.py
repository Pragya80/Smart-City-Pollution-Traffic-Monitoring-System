import streamlit as st

from frontend.components.analytics.correlation_chart import render_correlation_chart
from frontend.components.analytics.risk_zone_table import render_risk_zone_table
from frontend.components.pollution.aqi_cards import render_aqi_cards
from frontend.components.traffic.peak_hours_chart import render_peak_hours_chart
from frontend.services.api_client import get


def render_dashboard():
    st.title("Smart City Pollution & Traffic Monitoring")

    with st.expander("Connection", expanded=False):
        health = get("/health")
        st.json(health)

    city = st.selectbox("City", ["All", "Delhi", "Mumbai"], index=0)
    city_param = None if city == "All" else city

    col1, col2 = st.columns(2)
    with col1:
        pollution = get("/api/pollution/summary", params={"city": city_param} if city_param else {})
        render_aqi_cards(pollution)
    with col2:
        traffic = get("/api/traffic/summary", params={"city": city_param} if city_param else {})
        st.metric("Avg traffic density", traffic.get("avg_traffic_density"))
        st.metric("Avg speed", traffic.get("avg_speed"))

    st.divider()

    col3, col4 = st.columns(2)
    with col3:
        peak = get("/api/analytics/peak-hours", params={"city": city_param} if city_param else {})
        render_peak_hours_chart(peak)
    with col4:
        corr = get("/api/analytics/correlation", params={"city": city_param} if city_param else {})
        render_correlation_chart(corr)

    st.divider()
    risk = get("/api/analytics/high-risk-zones", params={"city": city_param} if city_param else {})
    render_risk_zone_table(risk)

