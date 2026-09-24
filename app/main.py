from app.market_data import get_market_data
from app.indicators import add_ema

def main():
    data = get_market_data("QQQ")
    
    data = add_ema(data, 20)
    data = add_ema(data, 50)
    data = add_ema(data, 200)


    print(data[["Close", "EMA_20", "EMA_50", "EMA_200"]].tail(10))


if __name__== "__main__":
    main()