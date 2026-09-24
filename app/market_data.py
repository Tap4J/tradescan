import yfinance as yf
import pandas as pd


def get_market_data(
    symbol: str,
    period: str = "1y",
    interval: str = "1d",
) -> pd.DataFrame:

    data = yf.download(
        symbol,
        period=period,
        interval=interval,
        auto_adjust=True,
        progress=False,
    )

    if data.empty:
        raise ValueError(f"No market data returned for {symbol}")

    # yfinance can return MultiIndex columns
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data[["Open", "High", "Low", "Close", "Volume"]].copy()

    return data