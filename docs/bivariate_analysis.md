## What Has Been Done — Bivariate Analysis

**Setup**
- Loaded cleaned dataset from `data/processed/clean_delivery_time.parquet`
- Used `matplotlib.use("Agg")` for headless figure generation
- Reused shared visualization utilities (`save_fig`, `set_labels`) for consistency across plots

**Plots Generated**
- Distance vs Delivery Time (scatter)
- Preparation Time vs Delivery Time (scatter)
- Courier Experience vs Delivery Time (scatter)
- Weather vs Delivery Time (boxplot)
- Traffic Level vs Delivery Time (boxplot)
- Time of Day vs Delivery Time (boxplot)
- Vehicle Type vs Delivery Time (boxplot)
- Correlation Heatmap (numeric features)

All figures saved to `outputs/bivariate_analysis/`.

---

### Distance vs Delivery Time
- There is a **clear positive correlation** between **delivery distance** and **delivery time**; as the distance increases, the delivery time generally increases.
- **Short-distance deliveries** (below **5,000 m**) are mostly completed within **15–50 minutes**.
- **Long-distance deliveries** (above **15,000 m**) exhibit **greater variability** in delivery time, ranging from approximately **45 to 150 minutes**.
- A few **outliers** have unusually high delivery times compared to other deliveries at similar distances, suggesting delays caused by factors other than distance.

### Preparation Time vs Delivery Time
- There is a **moderate positive relationship** between **preparation time** and **delivery time**; longer preparation times generally lead to longer overall delivery times.
- Orders with **short preparation times** (5–10 minutes) are mostly delivered within **15–60 minutes**.
- As **preparation time increases**, the **spread of delivery times also increases**, indicating greater variability in total delivery duration.
- A few **outliers** experienced exceptionally long delivery times (over **140 minutes**), even with moderate preparation times, suggesting that factors beyond preparation time also influence delivery performance.

### Courier Experience vs Delivery Time
- **Courier experience** shows **little to no clear relationship** with **delivery time**, as delivery times are widely distributed across all experience levels.
- Couriers at **every experience level** handled deliveries ranging from approximately **15 to 100 minutes**, indicating that experience alone is not a strong predictor of delivery time.
- A few **outliers** with delivery times exceeding **120 minutes** appear across multiple experience levels, suggesting delays caused by factors other than courier experience.
- The relatively uniform distribution of delivery times across experience levels indicates that **other variables**, such as distance, traffic, or weather conditions, likely have a greater impact on delivery performance.

### Weather vs Delivery Time
- **Snowy weather** has the **highest median delivery time**, indicating that deliveries generally take longer under snowy conditions.
- **Clear weather** has the **lowest median delivery time**, suggesting faster deliveries under favorable weather conditions.
- **Rainy, Foggy, and Windy** conditions have **similar delivery time distributions**, with only modest differences in their median values.
- The **variability in delivery time** is relatively similar across all weather conditions, although **Snowy weather** shows a slightly wider spread.
- A few **extreme delivery times** (outliers) are observed under **Clear, Rainy, and Windy** conditions, with some deliveries exceeding **120 minutes**.

### Traffic Level vs Delivery Time
- **High traffic** has the **highest median delivery time**, indicating that deliveries generally take longer under heavy traffic conditions.
- **Low traffic** has the **lowest median delivery time**, resulting in the fastest deliveries on average.
- **Medium traffic** falls between **High** and **Low** traffic in terms of median delivery time.
- Delivery times under **High** and **Medium** traffic show **greater variability** than those under **Low** traffic.
- A few **extreme delivery times** (outliers), exceeding **120 minutes**, are observed in both **Low** and **Medium** traffic conditions.

### Time of Day vs Delivery Time
- **Morning** has the **highest median delivery time**, indicating that deliveries tend to take slightly longer during this period.
- **Night** has the **lowest median delivery time**, suggesting relatively faster deliveries compared to other times of the day.
- **Afternoon**, **Evening**, and **Morning** have **similar delivery time distributions**, with only slight differences in their median values.
- Delivery times show **comparable variability** across all times of the day, indicating that time alone has a limited impact on delivery duration.
- A few **extreme delivery times** (outliers), exceeding **120 minutes**, are observed during the **Morning** and **Evening**.

### Vehicle Type vs Delivery Time
- **Bike, Car, and Scooter** have **very similar median delivery times**, indicating that vehicle type has only a minor effect on delivery duration.
- The **spread of delivery times** is comparable across all three vehicle types, suggesting similar variability in performance.
- **Scooters** exhibit the **highest maximum delivery times**, with a few deliveries exceeding **150 minutes**.
- **Bikes** and **Cars** also have several **high-duration outliers**, with delivery times exceeding **120 minutes**.
- Overall, **vehicle type does not appear to be a strong determinant of delivery time**.

### Correlation Heatmap (Numeric Features)
- **Distance** has a **strong positive correlation** with **delivery time** (**r = 0.78**), making it the strongest predictor among the numerical features.
- **Preparation time** has a **moderate positive correlation** with **delivery time** (**r = 0.31**), indicating that longer preparation generally leads to longer deliveries.
- **Courier experience** has a **very weak negative correlation** with **delivery time** (**r = -0.089**), suggesting almost no linear relationship.
- The correlations among the independent variables (**Distance**, **Preparation Time**, and **Courier Experience**) are **close to zero**, indicating little to no multicollinearity.
- Overall, **delivery distance** is the most influential numerical factor affecting delivery time, while **courier experience contributes very little**.

---

## What Will Be Done in Next Phase

- Finalize feature engineering plan based on confirmed strong predictors (`Distance_m`, `Traffic_Level`, `Weather`, `Preparation_Time_min`)
- Consider dropping or deprioritizing `Courier_Experience_yrs` and `Vehicle_Type` given their weak observed relationship with the target, or keep them for the model to weigh automatically (tree-based models handle weak features gracefully)