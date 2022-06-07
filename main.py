from flask import Flask, jsonify
from functions import get_ticker
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return '<h1>Hello, World!<h1>'

@app.route('/api/<ticker>/<interval>/<period>')
def Get_ticker(ticker, interval, period):
    r = get_ticker(ticker, interval, period)
    
    return jsonify(r)


if __name__ == '__main__':
    app.run(debug=True)