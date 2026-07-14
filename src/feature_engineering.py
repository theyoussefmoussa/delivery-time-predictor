import pandas as pd
import os
import sys
from dotenv import load_dotenv
project_root = os.path.abspath("..")
sys.path.insert(0, project_root)
load_dotenv()

def feature_engineering():
    # Loading Data
    BASE_PATH = os.getenv("BASE_PATH")
    OUTPUT_PATH = f"{BASE_PATH}/data/processed"
    df = pd.read_parquet(f"{BASE_PATH}/data/processed/clean_delivery_time.parquet")

    # Ordinal Encoding
    traffic_map = {'Low' : 0, 'Medium': 1, 'High' : 2}
    df['Traffic_Level'] = df['Traffic_Level'].map(traffic_map)

    # One Hot Encoding
    df = pd.get_dummies(df, columns=['Weather', 'Time_of_Day', 'Vehicle_Type'], drop_first=True)

    # Save Output
    df.to_parquet(f"{OUTPUT_PATH}/feature_engineering_clean_delivery_time.parquet")
    print(f"Number of Rows: {df.shape[0]}")
    print(f"Number of Columns: {df.shape[1]}")

    print("Done: feature_engineering.py")

if __name__ == "__main__": 
    feature_engineering()