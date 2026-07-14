import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import os
import sys
from dotenv import load_dotenv
project_root = os.path.abspath("..")
sys.path.insert(0, project_root)
from src.utils.visualization_utils import save_fig, set_labels
def bivariate_analysis():
    # Loading Data
    load_dotenv()
    BASE_PATH = os.getenv('BASE_PATH')
    OUTPUT_PATH = f"{BASE_PATH}/outputs/bivariate_analysis"
    df = pd.read_parquet(f"{BASE_PATH}/data/processed/clean_delivery_time.parquet")

    # Numeric Features vs Target 
    numeric_features = ['Distance_m', 'Preparation_Time_min', 'Courier_Experience_yrs']

    # Numeric Features vs Target 
    numeric_features = ['Distance_m', 'Preparation_Time_min', 'Courier_Experience_yrs']

    for col in numeric_features:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(data=df, x=col, y='Delivery_Time_min', ax=ax)
        set_labels(col)
        save_fig(fig, output_path=f"{OUTPUT_PATH}/{col}_vs_target.png")

    # Categorical Features
    categorical_features = ['Weather', 'Traffic_Level', 'Time_of_Day', 'Vehicle_Type']

    for col in categorical_features:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.boxplot(data=df, x=col, y='Delivery_Time_min', ax=ax)
        set_labels(col)
        save_fig(fig, output_path=f"{OUTPUT_PATH}/{col}_vs_target.png")

    # Heatmap for all numeric features
    numeric_cols = ['Distance_m', 'Preparation_Time_min', 'Courier_Experience_yrs', 'Delivery_Time_min']
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
    set_labels("Correlation Heatmap")
    save_fig(fig, output_path=f"{OUTPUT_PATH}/correlation_heatmap.png")

    print("Done: bivariate_analysis.py")
    print("All Graphs Saved in outputs/bivariate_analysis")


if __name__ == "__main__": 
    bivariate_analysis()