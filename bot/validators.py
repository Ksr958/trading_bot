def validate_side(side: str):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side.upper()

def validate_order_type(order_type: str):
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type.upper()

def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    return quantity
