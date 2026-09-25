import pandas as pd
from yfinance import data


def add_ema(data, period):
    data[f"EMA_{period}"] = data["Close"].ewm(span=period, adjust=False).mean()
    return data


def add_rsi(data, period=14):
    delta = data["Close"].diff()
    gain = delta.where(delta>0, 0)
    loss = delta.where(delta<0, 0).abs()

    avg_gain = gain.ewm(alpha=1/period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/period, adjust=False).mean()
    rs = avg_gain / avg_loss

    data[f"RSI_{period}"] = 100 - (100 / (1 + rs))

    return data

def add_atr(data, period=14):
    previous_close = data["Close"].shift(1)

    high_low = data["High"] - data["Low"]
    high_close = data["High"] - previous_close.abs()
    low_close = data["Low"] - previous_close.abs()

    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1/period, adjust=False).mean()
    
    data[f"ATR_{period}"] = atr
    
    return data