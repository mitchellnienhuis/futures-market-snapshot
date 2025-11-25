import pandas as pd
import os

# Streamlit Cloud runs from the repository root.
# So data files MUST be located relative to the app file, not module location.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_csv_contract(symbol: str) -> pd.DataFrame:
    filename = f"{symbol.lower()}.csv"
    path = os.path.join(DATA_DIR, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"CSV file not found at: {path}")

    df = pd.read_csv(path, parse_dates=['datetime'])
    df = df.sort_values('datetime').reset_index(drop=True)
    return df
