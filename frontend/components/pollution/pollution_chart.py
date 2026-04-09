import streamlit as st
import matplotlib.pyplot as plt


def show_pollution_chart(df):

    city_avg = (
        df.groupby("City")["AQI"]
        .mean()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots()

    city_avg.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Average AQI by City")

    ax.set_xlabel("City")

    ax.set_ylabel("AQI")

    st.pyplot(fig)