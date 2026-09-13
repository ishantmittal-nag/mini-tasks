from src.pricing import apply_discount, price_with_tier_discount


def checkout(order: dict) -> dict:
    """Compute the total for a raw order payload (e.g. a parsed request body)."""
    price = order["price"]
    if "customer_tier" in order:
        total = price_with_tier_discount(price, order["customer_tier"])
    else:
        discount_percent = order.get("discount_percent", 0)
        total = apply_discount(price, discount_percent)
    return {"total": total}
