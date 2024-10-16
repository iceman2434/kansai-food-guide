import pandas as pd
from config import DATA_FILE_PATH

def load_data():
    return pd.read_csv(DATA_FILE_PATH)