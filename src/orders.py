from src.discounts import bulk_discount_percent, stack_discounts
from src.inventory import InventoryStore
from src.loyalty import LoyaltyAccount
from src.pricing import apply_discount
from src.promotions import promo_discount


def price_order(order: dict) -> float:
    """Apply promo, then bulk-tier discount on top of the promo'd subtotal."""
    price = order["price"]
    promo_percent = promo_discount(order["promo_code"]) * 100 if "promo_code" in order else 0
    subtotal = apply_discount(price, promo_percent)
    bulk_percent = bulk_discount_percent(subtotal)
    return stack_discounts(subtotal, promo_percent, bulk_percent)


def place_order(
    order: dict,
    inventory: InventoryStore,
    loyalty: LoyaltyAccount,
    log: list = [],
) -> dict:
    total = price_order(order)

    if "sku" in order:
        inventory.reserve_stock(order["sku"], order.get("quantity", 1))

    loyalty.earn(total)
    log.append({"order": order, "total": total})
    return {"total": total, "log": log}


def place_bulk_orders(
    orders: list,
    inventory: InventoryStore,
    loyalty: LoyaltyAccount,
    log: list = [],
) -> list:
    return [place_order(order, inventory, loyalty, log) for order in orders]
