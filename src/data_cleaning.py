import pandas as pd
import numpy as np
import os 
from dotenv import load_dotenv

def data_cleaning():
    # Loading Data
    load_dotenv()
    BASE_PATH = os.getenv("BASE_PATH")
    df = pd.read_csv(f'{BASE_PATH}/data/raw/Food_Delivery_Times.csv')

    # Drop Identifier
    df.drop(columns=['Order_ID'], inplace=True)

    # drop duplicates if existed 
    df = df.drop_duplicates()

    # Downcast Categorical Columns
    categorical_columns = ['Weather', 'Traffic_Level', 'Time_of_Day', 'Vehicle_Type']
    for col in categorical_columns: 
        df[col] = df[col].astype('category')


    # fill categorical missing values with mode
    missing_columns = ['Weather', 'Traffic_Level','Time_of_Day']
    for col in missing_columns: 
        df[col]= df[col].fillna(df[col].mode()[0])


    # fill numeric column with median 
    df['Courier_Experience_yrs'] = df['Courier_Experience_yrs'].fillna(df['Courier_Experience_yrs'].median())

    # clip negative values to 0
    df.loc[df["Delivery_Time_min"] < 0, "Delivery_Time_min"] = 0

    # downcast Integer columns: 
    numeric_columns = ['Courier_Experience_yrs', 'Preparation_Time_min', 'Delivery_Time_min']
    for col in numeric_columns: 
        df[col] = df[col].astype('uint8') # range 0:255

    # Convert Distance to meter
    df["Distance_km"] = df["Distance_km"] * 1000
    df.rename(columns={"Distance_km": "Distance_m"}, inplace=True)
    
    # save new dataset
    output_path = f"{BASE_PATH}/data/processed/clean_delivery_time.parquet"
    df.to_parquet(
        path=output_path,
        index=False,
        engine="pyarrow"
    )
    print("Done: data_cleaning.py")
    print(f"new dataset is saved at: data/processed/clean_delivery_time.parquet")
    return df


if __name__ == "__main__":
    data_cleaning()