import yfinance as yf
import pandas as pd


def get_ticker(ticker, interval, period):
    interval = str(interval)
    period = str(period)
    ticker = str(ticker)
    ticker = ticker.upper()
    
    Stock = pd.DataFrame(yf.Ticker(ticker).history(period = period, interval=interval))
    df = Stock.reset_index()

    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

    df = df.set_index('Date')

    response = {
        'close': df['Close'].to_list(),
        'date': df.index.to_list()

    }

    response = formatting_response('date', 'close', response['date'], response['close'])
    return response

def get_holders(ticker):
    ticker = str(ticker)
    ticker = ticker.upper()
    Stock = yf.Ticker(ticker)
    df = Stock.major_holders
    
    percentage_holders = df.to_dict()[0]
    name_holders = df.to_dict()[1]
    
    t = len(name_holders)
    total_holders = int(percentage_holders[t-1])

    response = []
    for i in range(t-1):
        convert_porcentage = float( percentage_holders[i].replace("%", ""))/100
        obj = {
            "percentage": convert_porcentage * total_holders,
            "name": name_holders[i]
        }
        response.append(obj)

    return response

def formatting_response(p1, p2, item1, item2):
    array_obj = []
    for i in range(len(item1)):
        obj = {
            p2: item2[i],
            p1: item1[i],
        }
        array_obj.append(obj)
    return array_obj