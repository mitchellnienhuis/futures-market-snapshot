import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def load_csv_contract(symbol: str) -> pd.DataFrame:
    path = os.path.join(DATA_DIR, f"{symbol.lower()}.csv")
    df = pd.read_csv(path, parse_dates=['datetime'])
    df = df.sort_values('datetime').reset_index(drop=True)
    return df

