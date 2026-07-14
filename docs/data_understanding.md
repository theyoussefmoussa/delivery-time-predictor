## What Has Been Done — Data Understanding

**Dataset**
- Shape: `(1000, 9)`
- Duplicated rows: `0`
- Target variable: `Delivery_Time_min`
- Feature/target breakdown and column descriptions documented in `columns.md`

**Missing Values**

| Column                    | Missing Values |
|---------------------------|-----------------|
| `Weather`                  | 30              |
| `Traffic_Level`             | 30              |
| `Time_of_Day`               | 30              |
| `Courier_Experience_yrs`    | 30              |

**Data Types**
- Checked datatypes for each feature

**Numeric Columns**
- `describe()` reviewed — no outliers found initially

| Column                  | Min   | Max   |
|--------------------------|-------|-------|
| `Distance_km`             | 0.59  | 19.99 |
| `Preparation_Time_min`    | 5     | 29    |
| `Courier_Experience_yrs`  | 0.0   | 9.0   |

**Unique Values (Categorical Columns)**

| Column          | Unique Values                        |
|------------------|----------------------------------------|
| `Vehicle_Type`    | Bike, Scooter, Car                     |
| `Weather`         | Clear, Rainy, Foggy, Snowy, Windy      |
| `Time_of_Day`     | Morning, Afternoon, Evening, Night     |
| `Traffic_Level`   | Low, Medium, High                      |

---

## Next Phase — Data Cleaning

- Drop `Order_ID` (identifier column, no predictive value)
- Convert `Weather`, `Traffic_Level`, `Time_of_Day`, `Vehicle_Type` to `category` dtype
- Convert `Distance_km` to meters
- Downcast `Courier_Experience_yrs` and `Preparation_Time_min` to `int8`