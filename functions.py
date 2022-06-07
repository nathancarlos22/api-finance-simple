import yfinance as yf
import pandas as pd


def get_ticker(ticker, interval, period):
    interval = str(interval)
    period = str(period)
    ticker = str(ticker)
    ticker = ticker.upper()
    
    Stock = pd.DataFrame(yf.Ticker(ticker).history(period = period, interval=interval))
    df = Stock.reset_index()

    df['Date'] = pd.to_datetime(df['Date'])

    df = df.set_index('Date')

    response = {
        'ticker': ticker,
        'interval': interval,
        'period': period,
        'close': df['Close'].to_list(),
        'date': df.index.to_list()

    }

    return response