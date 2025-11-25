import pandas as pd
import os

# Get absolute path to THIS file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build absolute path to /data folder (one level up from /src)
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

def load_csv_contract(symbol: str) -> pd.DataFrame:
    # Normalize path (handles .. properly)
    data_path = os.path.normpath(os.path.join(DATA_DIR, f"{symbol.lower()}.csv"))

    print("Looking for CSV here:", data_path)  # Debug line

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Could not find file: {data_path}")

    df = pd.read_csv(data_path, parse_dates=['datetime'])
    df = df.sort_values('datetime').reset_index(drop=True)
    return df
