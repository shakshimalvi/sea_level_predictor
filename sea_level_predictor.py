import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # -------- First line of best fit (1880-2050) --------
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    x_pred = np.arange(df["Year"].min(), 2051)
    y_pred = result.slope * x_pred + result.intercept

    ax.plot(x_pred, y_pred, color="red")

    # -------- Second line (2000-2050) --------
    recent = df[df["Year"] >= 2000]

    result_recent = linregress(
        recent["Year"],
        recent["CSIRO Adjusted Sea Level"]
    )

    x_recent = np.arange(2000, 2051)
    y_recent = (
        result_recent.slope * x_recent
        + result_recent.intercept
    )

    ax.plot(x_recent, y_recent, color="green")

    # Labels
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save image
    plt.savefig("sea_level_plot.png")

    return plt.gca()