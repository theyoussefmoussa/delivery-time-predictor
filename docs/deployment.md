# Deployment

## What's Actually Done

- Model and scaler persisted with `joblib` to `models/linear_regression.pkl` and `models/scaler.pkl`, saved at the end of `modeling()` in `src/modeling.py`
- Streamlit app built at `app/app.py`:
  - Sidebar inputs: `Distance_m`, `Preparation_Time_min`, `Courier_Experience_yrs`, `Traffic_Level`, `Weather`, `Time_of_Day`, `Vehicle_Type`
  - Single input row manually encoded to match training feature order (`Traffic_Level` ordinal-mapped, `Weather`/`Time_of_Day`/`Vehicle_Type` one-hot with dropped baseline categories left as all-zero)
  - Numeric columns scaled with the saved `scaler` before prediction (`.transform()` only — no refitting)
  - Result rendered as a sentence with estimated arrival clock time, not a bare number
- Verified working locally via:
```bash
  streamlit run app/app.py
```
- App reads `BASE_PATH` from `.env`, consistent with the rest of the pipeline — no hardcoded paths

## Not Done Yet

- Not deployed to Streamlit Community Cloud — local run only for now
- No `requirements.txt` entry confirmed for `streamlit` / `joblib` (check before deploying)
- No input validation beyond Streamlit's built-in `min_value`/`max_value` bounds
- No handling for the model file being missing/corrupted (app will just crash with a raw traceback)

## Notes

- The dropped one-hot baseline categories (`Weather_Clear`, `Time_of_Day_Afternoon`, `Vehicle_Type_Bike`) are represented implicitly as all-zero rows in the app's encoding — this must stay in sync with whatever `pd.get_dummies(..., drop_first=True)` actually dropped in `feature_engineering.py`. If that encoding changes, `FEATURE_COLUMNS` and the baseline `if` checks in `app.py` need to be updated together, or predictions will silently be wrong.
- `FEATURE_COLUMNS` order in `app.py` is hardcoded to match `X_train.columns.tolist()` at training time — if features are added/removed later, this list must be regenerated and pasted in manually.
- UI went through two iterations: an initial gradient/card-based design, then a simplified professional version (sidebar inputs, neutral palette, single teal accent, sentence-based result) — current version is the latter.