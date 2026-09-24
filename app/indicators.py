import pandas as pd
from yfinance import data


def add_ema(data, period):
    data[f"EMA_{period}"] = data["Close"].ewm(span=period, adjust=False).mean()
    return data
