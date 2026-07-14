from src.data_cleaning import data_cleaning
from src.utils.formatting import separator
from src.eda.univariate_analysis import univariate_analysis
if __name__ == "__main__":
    print("Starting Phases")
    separator(title="Data Cleaning")
    data_cleaning()
    separator(title="Univariate Analysis")
    univariate_analysis()