from numpy.random import randn 
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd

# covid_visualization.py

import pandas as pd
import matplotlib.pyplot as plt

# 1) Load Data
def load_data(path="data/Covid Data.csv"):
    df = pd.read_csv(path)
    return df

# 2) Line Plot: Compare confirmed cases for top 5 countries
def plot_top5_countries(df):
    top5 = df.sort_values("total_confirmed", ascending=False).head(5)
    plt.figure(figsize=(10,6))
    plt.plot(top5["country"], top5["total_confirmed"], "ro--", label="Confirmed Cases")
    plt.title("Top 5 Countries - Confirmed Cases")
    plt.xlabel("Country")
    plt.ylabel("Confirmed Cases")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()

# 3) Bar Plot: Total confirmed by continent
def plot_by_continent(df):
    grouped = df.groupby("continent")[["total_confirmed"]].sum()
    grouped.plot(kind="bar", color="skyblue", legend=False)
    plt.title("Confirmed COVID-19 Cases by Continent")
    plt.ylabel("Confirmed Cases")
    plt.xticks(rotation=30)
    plt.show()

# 4) Custom Ticks & Labels
def plot_with_custom_ticks(df):
    top10 = df.sort_values("total_confirmed", ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(top10["country"], top10["total_confirmed"], "g^-", label="Confirmed")
    ax.set_title("Top 10 Countries - Custom Ticks Example")
    ax.set_xlabel("Countries")
    ax.set_ylabel("Confirmed Cases")
    ax.set_xticklabels(top10["country"], rotation=45, fontsize="small")
    ax.legend()
    plt.show()

# 5) Annotation Example
def plot_with_annotations(df):
    top = df.sort_values("total_confirmed", ascending=False).head(1)
    country = top["country"].values[0]
    cases = top["total_confirmed"].values[0]

    fig, ax = plt.subplots(figsize=(8,5))
    ax.bar(top["country"], top["total_confirmed"], color="orange")
    ax.set_title("Country with Highest Confirmed Cases")

    ax.annotate(f"Highest: {cases:,}", 
                xy=(0, cases), xytext=(0, cases+cases*0.1),
                ha="center", arrowprops=dict(facecolor="black", shrink=0.05))
    plt.show()

# 6) Shapes Example
def plot_with_shapes():
    fig, ax = plt.subplots()
    rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color="k", alpha=0.3)
    circ = plt.Circle((0.7, 0.2), 0.15, color="b", alpha=0.3)
    pgon = plt.Polygon([[0.15,0.15], [0.35,0.4], [0.2,0.6]], color="g", alpha=0.5)
    
    ax.add_patch(rect)
    ax.add_patch(circ)
    ax.add_patch(pgon)
    ax.set_title("Shapes Example (Rectangle, Circle, Polygon)")
    plt.show()

# -------------------------------
# Run All Plots
# -------------------------------
if __name__ == "__main__":
    df = load_data()

    plot_top5_countries(df)
    plot_by_continent(df)
    plot_with_custom_ticks(df)
    plot_with_annotations(df)
    plot_with_shapes()


