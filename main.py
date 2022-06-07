from flask import Flask, jsonify
from functions import get_ticker
# import sys
# sys.setrecursionlimit(10000)


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!<h1>'

@app.route('/api/<ticker>/<interval>/<period>')
def Get_ticker(ticker, interval, period):
    r = get_ticker(ticker, interval, period)
    
    return jsonify(r)


if __name__ == '__main__':
    app.run(debug=True)