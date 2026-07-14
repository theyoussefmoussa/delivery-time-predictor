import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import seaborn as sns
import sys
project_root = os.path.abspath("..")
sys.path.insert(0, project_root)
import matplotlib
matplotlib.use("Agg") # to not show the graph and just download
from src.utils.visualization_utils import (
    save_fig, 
    highlight_max_bar, 
    set_labels
    )
def univariate_analysis():
    load_dotenv()
    # Loading Data
    BASE_PATH = os.getenv("BASE_PATH")
    df = pd.read_parquet(f"{BASE_PATH}/data/processed/clean_delivery_time.parquet")
    OUTPUT_DIR = f"{BASE_PATH}/outputs/univariate_analysis"

    # Weather Distribution
    weather_counts = df['Weather'].value_counts()
    fig, ax = plt.subplots(figsize=(8,6))
    plt.pie(
        x=weather_counts,
        labels=weather_counts.index, # type: ignore
        autopct='%1.1f%%',
    )
    set_labels(title='Weather Counts')
    plt.tight_layout()
    plt.legend()
    save_fig(fig, output_path=f"{OUTPUT_DIR}/weather_distribution.png")

    # Traffic Level Distribution
    traffic_level_counts = df['Traffic_Level'].value_counts()
    fig, ax = plt.subplots(figsize=(8,6))
    sns.barplot(
            x=traffic_level_counts.index,
            y=traffic_level_counts.values )
    set_labels(title="Traffic Level", xlabel='Traffic Level', ylabel="Frequency")
    highlight_max_bar(ax)
    save_fig(fig, output_path=f"{OUTPUT_DIR}/traffic_level_distribution.png")

    # Time of Day Ditribution
    time_day_counts = df['Time_of_Day'].value_counts()
    fig, ax = plt.subplots(figsize=(8,6))
    sns.barplot(
            x=time_day_counts.index,
            y=time_day_counts.values )
    set_labels(title="Time of Day", xlabel='Time of Day', ylabel="Frequency")
    highlight_max_bar(ax)
    save_fig(fig, output_path=f"{OUTPUT_DIR}/time_of_day_distribution.png")

    # Vehicle Type Distribution
    vehicle_types_counts = df['Vehicle_Type'].value_counts()
    fig, ax = plt.subplots(figsize=(8,6))
    plt.pie(
        x=vehicle_types_counts.values, #type: ignore
        labels=vehicle_types_counts.index, #type: ignore
        autopct='%1.1f%%',
    )
    set_labels("Vehicle Type Distribution")
    plt.legend()
    save_fig(fig, output_path=f"{OUTPUT_DIR}/vehicle_type_distribution.png")

    # Preparation Time Counts
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="Preparation_Time_min",
        ax=ax
    )

    unique_vals = sorted(df["Preparation_Time_min"].unique())
    ax.set_xticks(range(0, len(unique_vals), 5))
    ax.set_xticklabels(unique_vals[::5])
    highlight_max_bar(ax)
    set_labels("Preparation Time Counts", "Preparation Time (Min)","Count")
    save_fig(fig, output_path=f"{OUTPUT_DIR}/preparation_time_counts.png")

    # Courier Experience Distribution
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="Courier_Experience_yrs",
        ax=ax
    )

    highlight_max_bar(ax)
    set_labels(
        "Courier Experience Distribution",
        "Courier Experience (Years)",
        "Count"
    )

    save_fig(fig, output_path=f"{OUTPUT_DIR}/courier_experience_counts.png")

    print("Done: univariate_analysis.py")
    print(f"All Graphs Saved in outputs/univariate_analysis")


if __name__ == '__main__': 
    univariate_analysis()