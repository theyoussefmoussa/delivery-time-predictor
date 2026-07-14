from src.data_cleaning import data_cleaning
from src.utils.formatting import separator
if __name__ == "__main__":
    print("Starting Phases")
    separator(title="Data Cleaning")
    data_cleaning()
    separator()
