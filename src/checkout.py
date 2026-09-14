from src.inventory import InventoryStore
from src.pricing import apply_discount
from src.promotions import promo_discount


def checkout(order: dict, inventory: InventoryStore | None = None) -> dict:
    """Compute the total for a raw order payload (e.g. a parsed request body)."""
    price = order["price"]
    if "promo_code" in order:
        discount_percent = promo_discount(order["promo_code"]) * 100
    else:
        discount_percent = order.get("discount_percent", 0)
    total = apply_discount(price, discount_percent)

    if inventory is not None and "sku" in order:
        quantity = order.get("quantity", 1)
        inventory.reserve_stock(order["sku"], quantity)

    return {"total": total}
