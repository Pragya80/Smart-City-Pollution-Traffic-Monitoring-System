import pandas as pd
import streamlit as st


def render_risk_zone_table(payload: dict):
    st.subheader("High risk zones")
    items = payload.get("items") or []
    if not items:
        st.info("No risk zone data available.")
        return

    df = pd.DataFrame(items)
    st.dataframe(df, use_container_width=True, hide_index=True)

