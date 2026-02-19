import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client
