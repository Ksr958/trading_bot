import argparse
import logging
from bot.client import BinanceFuturesClient
from bot.orders import OrderService
from bot.validators import validate_side, validate_order_type, validate_quantity
from bot.logging_config import setup_logger

def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        if order_type == "LIMIT" and not args.price:
            raise ValueError("LIMIT orders require --price")

        client = BinanceFuturesClient().get_client()
        order_service = OrderService(client)

        print("\n--- Order Request Summary ---")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if args.price:
            print(f"Price: {args.price}")
        response = order_service.place_order(
            symbol=args.symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=args.price
        )

        print("\n--- Order Response ---")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
        print("\n✅ Order placed successfully!")

    except Exception as e:
        logging.error(str(e))
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
