from functions import *
import json

def write_ticker_file(tickers, interval, period,upgrade=False):
    
    with open('data/tickers.json','w',encoding='utf-8') as file:
        if upgrade: 
            result = get_tickers(tickers, interval, period)
            file.write(json.dumps(result))

if __name__ == "__main__":
    # Teste
    tickers = "AMZN;TSLA;AAPL;PETR4.SA"
    interval = "1d"
    period = "1y"

    write_ticker_file(tickers, interval, period,upgrade=True)