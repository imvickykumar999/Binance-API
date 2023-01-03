
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/asset_balance')
def asset_balance():
    import fetch
    val1 = fetch.asset_balance()
    return render_template('asset_balance.html', val=val1)

@app.route('/symbol_ticker')
def symbol_ticker():
    import fetch
    val2 = fetch.symbol_ticker()
    return render_template('symbol_ticker.html', val=val2)

@app.route('/topost', methods=['POST'])
def symbol_info():
    return render_template('symbol_info.html')

if __name__ == '__main__':
    app.run(debug=True)