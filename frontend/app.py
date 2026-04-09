from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

# Ensure repo root is importable when running via:
#   streamlit run frontend/app.py
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from frontend.pages.dashboard import render_dashboard  # noqa: E402


def main():
    st.set_page_config(
        page_title="Smart City Dashboard",
        layout="wide",
    )

    st.sidebar.title("Smart City Monitoring")
    page = st.sidebar.radio("Navigate", ["Dashboard"], index=0)

    if page == "Dashboard":
        render_dashboard()


if __name__ == "__main__":
    main()

