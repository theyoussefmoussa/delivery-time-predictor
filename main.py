from src.data_cleaning import data_cleaning
from src.utils.formatting import separator
from src.eda.univariate_analysis import univariate_analysis
from src.eda.bivariate_analysis import bivariate_analysis
from src.feature_engineering import feature_engineering
from src.model import modeling
if __name__ == "__main__":
    print("Starting Phases")
    separator(title="Data Cleaning")
    data_cleaning()
    separator(title="Univariate Analysis")
    univariate_analysis()
    separator(title="Bivariate Analysis")
    bivariate_analysis()
    separator(title="Feature Engineering")
    feature_engineering()
    separator(title="Linear Regression Model")
    modeling()