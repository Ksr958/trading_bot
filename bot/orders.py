import logging
from binance.exceptions import BinanceAPIException

logger = logging.getLogger(__name__)

class OrderService:
    def __init__(self, client):
        self.client = client

    def configure_symbol(self, symbol, leverage):
        logger.info(f"Setting leverage {leverage}x for {symbol}")
        self.client.futures_change_leverage(
            symbol=symbol,
            leverage=leverage
        )
    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            self.configure_symbol(symbol, 10)
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            if order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price is required for LIMIT orders")

                params["price"] = price
                params["timeInForce"] = "GTC"

            elif order_type != "MARKET":
                raise ValueError("Unsupported order type")

            # ✅ Log request
            logger.info(f"Sending Order: {params}")

            response = self.client.futures_create_order(**params)

            # ✅ Log response
            logger.info(f"Order Response: {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"API Error: {e.message} (Code: {e.code})")
            raise

        except Exception as e:
            logger.exception("Unexpected error occurred while placing order")
            raise
