# frontend/components/analytics/risk_zone_table.py
import streamlit as st
import pandas as pd


def render_risk_zone_table(df: pd.DataFrame):
    st.subheader("🔴 High Risk Zones")
    st.dataframe(df)