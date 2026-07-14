<p align="center">
  <img src="assets/banner_image.png" alt="Delivery Time Predictor Banner" width="100%">
</p>

<h1 align="center">Delivery Time Predictor</h1>

<p align="center">
  Predicting food delivery time using distance, weather, traffic, and courier experience data — an end-to-end machine learning pipeline from data cleaning to modeling.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=flat&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/scikit--learn-Modeling-F7931E?style=flat&logo=scikitlearn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=flat&logo=plotly&logoColor=white" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-Visualization-3776AB?style=flat" alt="Seaborn">
  <img src="https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=flat&logo=jupyter&logoColor=white" alt="Jupyter">
</p>

---

## Current Status

**Phase 2 — Data Cleaning** (in progress)

- [x] Phase 1 — Data Understanding
- [ ] Phase 2 — Data Cleaning
- [ ] Phase 3 — Feature Engineering
- [ ] Phase 4 — Exploratory Data Analysis
- [ ] Phase 5 — Modeling
- [ ] Phase 6 — Evaluation & Deployment

Progress and phase-by-phase notes are documented in [`docs/`](docs/).

---

## Project Structure

```
delivery-time-predictor/
├── assets/                    # Images and banner
├── data/
│   ├── raw/                   # Original, immutable data
│   └── processed/             # Cleaned and transformed data
├── src/                       # Source code (cleaning, features, etc.)
├── notebooks/
│   └── 1_data_understanding/  # Exploration notebooks
├── docs/
│   └── data_understanding.md  # Phase-by-phase documentation
├── models/                    # Trained model artifacts
├── app/                       # Application / deployment code
├── columns.md                 # Feature and target descriptions
├── pipelines.md                # Pipeline documentation
├── requirements.txt
├── main.py
└── README.md
```

---

## Getting Started

```bash
git clone https://github.com/theyoussefmoussa/delivery-time-predictor.git
cd delivery-time-predictor
pip install -r requirements.txt
```

---

## Dataset

The dataset contains delivery records with features such as distance, weather conditions, traffic level, time of day, vehicle type, and courier experience. Target variable: `Delivery_Time_min`.

Full feature documentation available in [`columns.md`](columns.md).

---

## Contact

**Youssef Moussa**

<p>
  <a href="https://github.com/theyoussefmoussa"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="https://linkedin.com/in/theyoussefmoussa"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://kaggle.com/theyoussefmoussa"><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=flat&logo=kaggle&logoColor=white" alt="Kaggle"></a>
</p>