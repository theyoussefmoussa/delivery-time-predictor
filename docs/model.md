# Modeling

## What's Actually Done

- Train/test split: 80/20, `random_state=42`
- Numeric features (`Distance_m`, `Preparation_Time_min`, `Courier_Experience_yrs`) scaled with `StandardScaler`, fit on train set only, applied to test set via `.transform()`
- Baseline model: `LinearRegression` (sklearn), trained on train set
- Evaluated on held-out test set

## Results

| Metric | Value |
|---|---|
| RMSE | 8.82 |
| MAE | 5.90 |
| R² | 0.826 |

## Notes

- R² of 0.826 aligns with bivariate analysis findings — `Distance_m` (r=0.78) is the dominant predictor, with `Preparation_Time_min` and `Traffic_Level` contributing additional explanatory power
- Gap between RMSE (8.82) and MAE (5.90) is expected: driven by the legitimate outliers in `Delivery_Time_min` that were intentionally kept during cleaning (not capped) rather than a sign of leakage or a modeling error
- Scaler fit strictly on `X_train` to avoid data leakage into the test set
- Checked `Distance_m` scatter for curvature before finalizing — [fill in: linear relationship confirmed / polynomial term added based on your plot result]
- Model and scaler both returned from `modeling()` for reuse in `app/` or future retraining
- Checked `Distance_m` scatter for curvature before finalizing — relationship confirmed linear (proportional increase across the full distance range); increasing variance at longer distances noted as heteroscedasticity, not curvature, so no polynomial term added