
from binance.client import Client
import math

client = Client('YCMCERkmFNSSIK2pF4MaKkffsY10EYtgzpCdn5mMAybqBslTXej6gGZ4e1ORRAzO', 
'PE03qLBcdlFlqGTXucbZpS4qcODYePN9OdP0Vurp9T8n52xKEDKMJ3GQA5kBclsC')

def asset_balance():
    client.API_URL = 'https://testnet.binance.vision/api'
    return client.get_asset_balance(asset='BTC')


def symbol_ticker():
    btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
    return (btc_price)

def symbol_info():
    symbol_info = client.get_symbol_info('BTCUSDT')
    step_size = 0.0
    for f in symbol_info['filters']:
        if f['filterType'] == 'LOT_SIZE':
            step_size = float(f['stepSize'])

    trade_size = 10
    sym = 'BTCUSDT'
    tick_size = 6
    price = 19000

    trade_quantity = trade_size / price
    quantity = "{:0.0{}f}".format(trade_quantity, tick_size)

    precision = int(round(-math.log(step_size, 10), 0))
    quantity = float(quantity)

    client.futures_create_order(symbol=sym, side='BUY', type='MARKET', quantity=quantity)
