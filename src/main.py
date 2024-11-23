# src/main.py
import time
import yfinance as yf
from logger import get_logger

logger = get_logger()

class BitcoinTrader:
    def __init__(self):
        self.asset_id = 'BTC-USD'  # Yahoo Finance notation for Bitcoin

    def fetch_price(self):
        try:
            data = yf.Ticker(self.asset_id)
            hist = data.history(period="1d", interval="1m")  # Fetch daily data
            last_close = hist['Close'].iloc[-1]  # Get the last close price
            return last_close
        except Exception as e:
            logger.error(f"Error fetching Bitcoin price: {e}")
            return None

    def run(self):
        while True:
            price = self.fetch_price()
            if price:
                logger.info(f"Current Bitcoin price: {price}")
                # Example: Placeholder for trading logic
            else:
                logger.info("No price data available.")
            time.sleep(5)  # Sleep for a minute between checks

if __name__ == '__main__':
    trader = BitcoinTrader()
    trader.run()