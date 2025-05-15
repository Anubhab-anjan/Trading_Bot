from alpaca.data import StockHistoricalDataClient, StockBarsRequest, TimeFrame
from datetime import datetime, timedelta
import pytz

API_KEY = "PKCOJ5IJC6JC2YYLS6BX"
SECRET_KEY = "YwPfFA0IOJZycIoajWFCJLHMyjkpae0eaUCz2zxs"
SYMBOLS = ["AAPL", "MSFT", "TSLA", "AMZN", "GOOGL"]


def get_historical_bars():
    client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

    eastern = pytz.timezone("US/Eastern")
    today = eastern.localize(datetime.now())
    start = today - timedelta(days=3)
    end = start + timedelta(hours=0.5)

    start_utc = start.astimezone(pytz.utc)
    end_utc = end.astimezone(pytz.utc)

    request_params = StockBarsRequest(
        symbol_or_symbols=SYMBOLS,
        timeframe=TimeFrame.Minute,
        start=start_utc,
        end=end_utc,
        adjustment='raw',
        feed="sip"
    )

    try:
        bars = client.get_stock_bars(request_params)

        if bars and bars.data:
            print("\nHistorical data retrieved successfully:")
            for symbol, bar_set in bars.data.items():
                print(f"\n{symbol} - {len(bar_set)} bars available")
                print("Sample bars:")
                for bar in bar_set[:3]:
                    print(f"  {bar.timestamp} | O:{bar.open} H:{bar.high} L:{bar.low} C:{bar.close}")
        else:
            print("No data returned for the specified time range")

    except Exception as e:
        print(f"Error fetching historical data: {e}")


if __name__ == "__main__":
    get_historical_bars()