import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
from dotenv import load_dotenv
import os

import joblib
load_dotenv()
BASE_PATH = os.getenv("BASE_PATH")
def modeling():
    df = pd.read_parquet(f"{BASE_PATH}/data/processed/feature_engineering_clean_delivery_time.parquet")

    X = df.drop(columns="Delivery_Time_min")
    y = df["Delivery_Time_min"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    numeric_cols = ['Distance_m', 'Preparation_Time_min', 'Courier_Experience_yrs']
    X_train[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
    X_test[numeric_cols] = scaler.transform(X_test[numeric_cols])

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"RMSE: {rmse:.2f} | MAE: {mae:.2f} | R2: {r2:.3f}")

    joblib.dump(model, f"{BASE_PATH}/models/linear_regression.pkl")
    joblib.dump(scaler, f"{BASE_PATH}/models/scaler.pkl")
    
    return model, scaler


if __name__ == "__main__":
    modeling()