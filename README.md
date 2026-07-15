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

**Finished - UnderReview** (in progress)

- [x] Phase 1 — Data Understanding
- [x] Phase 2 — Data Cleaning
- [x] Phase 3 — Exploratory Data Analysis
- [x] Phase 4 — Feature Engineering
- [x] Phase 5 — Modeling
- [x] Phase 6 — Evaluation & Deployment

Progress and phase-by-phase notes are documented in [`docs/`](docs/).

---

## Project Structure

```
delivery-time-predictor/
├── assets/
│   └── banner_image.png
├── data/
│   ├── raw/                        # Original, immutable data
│   └── processed/                  # Cleaned and transformed data
├── src/                            # Source code (cleaning, features, etc.)
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── eda/
│   │   └── univariate_analysis.py
│   │   └── bivariate_analysis.py
│   └── utils/
│       ├── formatting.py
│       └── visualization_utils.py
├── notebooks/
│   ├── 1_data_understanding.ipynb
│   ├── 2_data_cleaning.ipynb
│   └── 3_univariate_analysis.ipynb
│   └── 4_bivariate_analysis.ipynb
│   └── 5_feature_engineering.ipynb
├── docs/
│   ├── data_understanding.md       # Phase-by-phase documentation
│   ├── data_cleaning.md
│   └── univariate_analysis.md
│   └── bivariate_analysis.md
│   └── feature_engineering.md
│   └── model.md
├── models/                         # Trained model artifacts
├── app/                            # Application / deployment code
├── columns.md                      # Feature and target descriptions
├── pipelines.md                    # Pipeline documentation
├── requirements.txt
├── .env.example                    # Template for required environment variables
├── .gitignore
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

## Contact Team

## Contact Team
| Name | Role | GitHub | LinkedIn |
|---|---|---|---|
| **Youssef Moussa** | Team Leader | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/theyoussefmoussa) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/theyoussefmoussa) |
| **Aliaa Abdallah** | Member | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/aliaaabdallah) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aliaa-abdallah-624682422) |
| **Habiba Saad** | Member | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/habebayoussef) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/habiba-saad-6ba769351) |
| **Youssef Shaban** | Member | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/youssefbadwi) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/youssef-shabban-800904277) |
| **Mostafa Ibrahim** | Member | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/mostafamawazen99-code) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mostafa-ibrahim-9b9737347) |


