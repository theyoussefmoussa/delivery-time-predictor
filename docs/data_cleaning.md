## What Has Been Done — Data Cleaning

**Loading**
- Data loaded from `data/raw/Food_Delivery_Times.csv` using `BASE_PATH` env variable (`python-dotenv`) for cross-device compatibility

**Identifier & Duplicates**
- Dropped `Order_ID` (identifier column, no predictive value)
- Checked and dropped duplicate rows (run *after* dropping `Order_ID`, since the identifier would otherwise make every row artificially unique)

**Data Types**
- Converted `Weather`, `Traffic_Level`, `Time_of_Day`, `Vehicle_Type` to `category` dtype

**Missing Values**

| Column | Strategy | Reason |
|---|---|---|
| `Weather` | Mode | Categorical, missingness scattered (not systematic) |
| `Traffic_Level` | Mode | Categorical, missingness scattered |
| `Time_of_Day` | Mode | Categorical, missingness scattered |
| `Courier_Experience_yrs` | Median | Numeric, more robust to skew than mean |

*Note: missingness pattern was checked prior to imputation — confirmed scattered across independent rows (114 rows with 1 missing column, 3 rows with 2), not a single systematic collection failure. This justified per-column imputation over row dropping.*

**Invalid Values**
- Negative values in `Delivery_Time_min` clipped to `0`

**Outlier Investigation**
- IQR method applied across all numeric columns
- `Delivery_Time_min` outliers (values > ~115 min) investigated individually — all traced to logical causes: long `Distance_km`, poor `Weather`, high `Traffic_Level`, or low `Courier_Experience_yrs`
- **Decision: outliers kept, not capped or dropped** — since `Delivery_Time_min` is the target variable, these rows carry real signal the model needs to learn (e.g., worst-case delivery conditions), rather than representing data errors

**Downcasting**
- `Courier_Experience_yrs`, `Preparation_Time_min`, `Delivery_Time_min` downcast to `uint8` (range 0–255) — confirmed safe after outlier investigation showed true max ≈155, well within range

**Output**
- Cleaned dataset saved to `data/processed/clean_delivery_time.parquet` (`pyarrow` engine)
- Implemented as `data_cleaning()` function in `src/`, with `if __name__ == "__main__":` guard

---

## What Will Be Done in Next Phase

- Feature engineering (e.g., encoding categorical variables for modeling, potential interaction features between `Distance_km` / `Traffic_Level` / `Weather`)
- Train/test split strategy
- Baseline model selection