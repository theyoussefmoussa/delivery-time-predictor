## What Has Been Done — Feature Engineering

**Loading**
- Loaded cleaned dataset from `data/processed/clean_delivery_time.parquet`

**Encoding**

| Column | Method | Reason |
|---|---|---|
| `Traffic_Level` | Ordinal (`Low`=0, `Medium`=1, `High`=2) | Natural order confirmed relevant in bivariate analysis (higher traffic → higher delivery time) |
| `Weather`, `Time_of_Day`, `Vehicle_Type` | One-hot (`drop_first=True`) | Nominal categories, no inherent order; drop-first avoids dummy variable trap for linear modeling |

**Scaling**
- Not performed in this phase — deferred to modeling phase to avoid data leakage (scaler must be fit on train set only, after train/test split)

**Output**
- Feature-engineered dataset saved to `data/processed/feature_engineering_clean_delivery_time.parquet`
- Implemented as `feature_engineering()` function in `src/`, with `if __name__ == "__main__":` guard
- Row/column counts printed for verification after transformation

---

## What Will Be Done in Next Phase

- Train/test split
- Fit `StandardScaler` on numeric columns (`Distance_m`, `Preparation_Time_min`, `Courier_Experience_yrs`) using train set only
- Train baseline Linear Regression model
- Evaluate using RMSE, MAE, R²