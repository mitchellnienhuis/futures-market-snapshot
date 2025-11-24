import pandas as pd

def compute_daily_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['date'] = df['datetime'].dt.date
    agg = df.groupby('date').agg(
        open=('open','first'),
        high=('high','max'),
        low=('low','min'),
        close=('close','last'),
        volume=('volume','sum'),
    ).reset_index()
    agg['prev_close'] = agg['close'].shift(1)
    agg['return_close_to_close'] = (agg['close'] / agg['prev_close'] - 1).fillna(0)
    agg['overnight'] = (agg['open'] / agg['prev_close'] - 1).fillna(0)
    agg['sma_5'] = agg['close'].rolling(5).mean()
    agg['sma_20'] = agg['close'].rolling(20).mean()
    agg['sma5_sma20_diff'] = agg['sma_5'] - agg['sma_20']
    return agg
