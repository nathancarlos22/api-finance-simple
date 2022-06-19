from flask import Flask, jsonify
from functions import *
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return '<h1>Request: https://api-finance-simple.herokuapp.com/api/simbolo/intervalo/periodo<h1><h2>Exemplo de uso: https://api-finance-simple.herokuapp.com/api/BOVA11.SA/1d/6mo</h2> <p>OBS: Use a extensão JSON VIEWER</p>'

@app.route('/api/<ticker>/<interval>/<period>')
def Get_ticker(ticker, interval, period):
    r = get_ticker(ticker, interval, period)
    
    return jsonify(r)
    
@app.route('/api/tickers/<tickers>/<interval>/<period>')
def Get_tickers(tickers,interval, period):
    r = get_tickers(tickers,interval, period)
    
    return jsonify(r)

@app.route('/api/holders/<ticker>')
def Get_holders(ticker):
    r = get_holders(ticker)
    
    return jsonify(r)

@app.route('/api/dividend/<ticker>')
def Get_dividend(ticker):
    r = get_dividends(ticker)
    
    return jsonify(r)

@app.route('/api/dividends/<tickers>')
def Get_dividends(tickers):
    r = get_dividends(tickers)
    
    return jsonify(r)

if __name__ == '__main__':
    app.run(debug=True)