## What Has Been Done — Univariate Analysis

**Setup**
- Loaded cleaned dataset from `data/processed/clean_delivery_time.parquet`
- Used `matplotlib.use("Agg")` for headless figure generation
- Reused shared visualization utilities (`save_fig`, `highlight_max_bar`, `set_labels`) for consistency across plots

**Plots Generated**
- Weather distribution (pie chart)
- Traffic Level distribution (bar chart)
- Time of Day distribution (bar chart)
- Vehicle Type distribution (pie chart)
- Preparation Time distribution (count plot)
- Courier Experience distribution (count plot)

All figures saved to `outputs/univariate_analysis/`.

---

### Weather Distribution
- Nearly **half of all orders** were placed under **Clear** weather conditions.
- Approximately **one in five orders** occurred during **Rainy** weather.
- About **one in ten orders** were placed during **Foggy** weather.
- **Snowy** and **Windy** weather accounted for nearly identical shares, at approximately **9.7% each**.

### Traffic Level Distribution
- About **40% of all orders** were placed under **Medium** traffic conditions.
- Approximately **36% of orders** occurred during **Low** traffic conditions.
- Roughly **one in five orders** were placed during **High** traffic conditions.

### Time of Day Distribution
- Approximately **one in three orders** were placed during the **Morning**.
- **Afternoon** and **Evening** had **almost identical order volumes**, with approximately **275 orders** each.
- Only **about 8% of orders** were placed during the **Night**.

### Vehicle Type Distribution
- Approximately **50.03% of all orders** were delivered by **Bike**.
- Around **30.2% of orders** were delivered by **Scooter**.
- The remaining **19.5% of orders** were delivered by **Car**.

### Preparation Time Distribution
- **Preparation times are fairly evenly distributed** across the range of **5 to 29 minutes**, with no strong concentration at a specific duration.
- The **highest number of orders** occurred at a **preparation time of 14 minutes**, with approximately **52 orders**.
- Most preparation times recorded **between 35 and 50 orders**, indicating a relatively balanced distribution.
- Preparation times of **15 and 18 minutes** had the **lowest order counts**, with fewer than **30 orders** each.

### Courier Experience Distribution
- The **highest number of orders** was handled by couriers with **5 years of experience**, with approximately **120 orders**.
- Order counts are **fairly evenly distributed** across all experience levels, indicating no strong dependence on courier experience.
- Couriers with **3 years of experience** handled the **fewest orders**, with around **80 orders**.
- Most experience levels accounted for **90 to 110 orders**, suggesting a balanced allocation of deliveries among couriers.

---

## What Will Be Done in Next Phase

- Bivariate analysis: relationship between each feature and `Delivery_Time_min`
- Investigate `Traffic_Level`, `Weather`, and `Distance_km` as likely strongest predictors
- Check for correlation and multicollinearity among numeric features
