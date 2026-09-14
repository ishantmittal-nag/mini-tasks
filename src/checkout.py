from src.inventory import InventoryStore
from src.pricing import apply_discount
from src.promotions import promo_discount, redeem_gift_card, shipping_rate_for_method


def checkout(order: dict, inventory: InventoryStore | None = None) -> dict:
    """Compute the total for a raw order payload (e.g. a parsed request body)."""
    price = order["price"]
    if "promo_code" in order:
        discount_percent = promo_discount(order["promo_code"]) * 100
    else:
        discount_percent = order.get("discount_percent", 0)
    total = apply_discount(price, discount_percent)

    if "gift_card_code" in order:
        total -= redeem_gift_card(order["gift_card_code"])

    if "shipping_method" in order:
        total += shipping_rate_for_method(order["shipping_method"])

    if inventory is not None and "sku" in order:
        quantity = order.get("quantity", 1)
        inventory.reserve_stock(order["sku"], quantity)

    return {"total": total}


def checkout_cart(cart: dict, inventory: InventoryStore) -> dict:
    """Compute the total for a multi-line-item cart payload and reserve stock for it."""
    items = cart["items"]
    total = sum(item["price"] * item.get("quantity", 1) for item in items)
    inventory.bulk_reserve(items)
    return {"total": total}
