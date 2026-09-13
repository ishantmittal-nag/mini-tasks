from src.pricing import apply_discount


def checkout(order: dict) -> dict:
    """Compute the total for a raw order payload (e.g. a parsed request body)."""
    price = order["price"]
    discount_percent = order.get("discount_percent", 0)
    total = apply_discount(price, discount_percent)
    return {"total": total}
