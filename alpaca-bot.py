from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

from datetime import datetime, timedelta
import pandas as pd
import pytz
import time

API_KEY = "YOUR_API_KEY"
SECRET_KEY = "YOUR_SECRET_KEY"

SYMBOLS = ["AAPL", "MSFT", "TSLA"]

SHORT_WINDOW = 5
LONG_WINDOW = 20

STOP_LOSS = 0.97
TAKE_PROFIT = 1.05

historical_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)
trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

positions = {}

def get_data(symbol):
    eastern = pytz.timezone("US/Eastern")

    end = eastern.localize(datetime.now())
    start = end - timedelta(days=5)

    request = StockBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=TimeFrame.Minute,
        start=start.astimezone(pytz.utc),
        end=end.astimezone(pytz.utc),
        adjustment="raw",
        feed="sip"
    )

    bars = historical_client.get_stock_bars(request)

    data = []

    for bar in bars.data[symbol]:
        data.append({
            "time": bar.timestamp,
            "close": bar.close
        })

    df = pd.DataFrame(data)

    return df


def generate_signal(df):
    df["short_ma"] = df["close"].rolling(SHORT_WINDOW).mean()
    df["long_ma"] = df["close"].rolling(LONG_WINDOW).mean()

    latest = df.iloc[-1]

    if latest["short_ma"] > latest["long_ma"]:
        return "BUY"

    elif latest["short_ma"] < latest["long_ma"]:
        return "SELL"

    return "HOLD"


def place_buy_order(symbol, qty):
    order = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY
    )

    trading_client.submit_order(order)

    latest_price = get_latest_price(symbol)

    positions[symbol] = {
        "buy_price": latest_price,
        "qty": qty
    }

    print(f"BUY ORDER PLACED: {symbol} at {latest_price}")


def place_sell_order(symbol, qty):
    order = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=OrderSide.SELL,
        time_in_force=TimeInForce.DAY
    )

    trading_client.submit_order(order)

    latest_price = get_latest_price(symbol)

    buy_price = positions[symbol]["buy_price"]

    profit = (latest_price - buy_price) * qty

    print(f"SELL ORDER PLACED: {symbol}")
    print(f"Profit/Loss: {profit:.2f}")

    del positions[symbol]


def get_latest_price(symbol):
    df = get_data(symbol)
    return df.iloc[-1]["close"]


def risk_management(symbol):
    if symbol not in positions:
        return

    current_price = get_latest_price(symbol)

    buy_price = positions[symbol]["buy_price"]

    if current_price <= buy_price * STOP_LOSS:
        print(f"STOP LOSS HIT: {symbol}")
        place_sell_order(symbol, positions[symbol]["qty"])

    elif current_price >= buy_price * TAKE_PROFIT:
        print(f"TAKE PROFIT HIT: {symbol}")
        place_sell_order(symbol, positions[symbol]["qty"])


def run_bot():
    while True:
        try:
            for symbol in SYMBOLS:

                print(f"\nChecking {symbol}")

                df = get_data(symbol)

                signal = generate_signal(df)

                print(f"Signal: {signal}")

                if signal == "BUY" and symbol not in positions:
                    place_buy_order(symbol, 1)

                elif signal == "SELL" and symbol in positions:
                    place_sell_order(symbol, positions[symbol]["qty"])

                risk_management(symbol)

            print("\nSleeping for 60 seconds...\n")

            time.sleep(60)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)


if __name__ == "__main__":
    run_bot()
