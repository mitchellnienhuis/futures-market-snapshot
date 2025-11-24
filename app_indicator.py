import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


import streamlit as st
from datetime import datetime
from src.data_loader import load_csv_contract
from src.feature_engineering import compute_daily_features
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="Futures Snapshot — Indicators")
st.title("Futures Market Snapshot — Indicators")

symbols = ["mes","mnq"]
cols = st.columns(len(symbols))

for i, sym in enumerate(symbols):
    df = load_csv_contract(sym)
    daily = compute_daily_features(df)
    today = daily.iloc[-1]
    with cols[i]:
        st.header(sym.upper())
        bias = "Neutral"
        if today['sma_5'] > today['sma_20'] and today['return_close_to_close'] > 0:
            bias = "Bullish"
        elif today['sma_5'] < today['sma_20'] and today['return_close_to_close'] < 0:
            bias = "Bearish"
        st.metric("Bias", bias)

        recent = df.set_index('datetime').last('14D').reset_index()
        fig = go.Figure(data=[go.Candlestick(
            x=recent['datetime'], open=recent['open'], high=recent['high'],
            low=recent['low'], close=recent['close']
        )])
        fig.update_layout(height=300, margin=dict(t=25,b=10,l=10,r=10))
        st.plotly_chart(fig, use_container_width=True)

