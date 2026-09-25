from app.market_data import get_market_data
from app.indicators import add_ema, add_rsi, add_atr


def main():
    data = get_market_data("QQQ")
    
    data = add_ema(data, 20)
    data = add_ema(data, 50)
    data = add_ema(data, 200)

    data = add_rsi(data, 14)
    data = add_atr(data, 14)

    print(data[["Close", "EMA_20", "EMA_50", "EMA_200", "RSI_14", "ATR_14"]].tail(10))


if __name__== "__main__":
    main()