from src.inventory import InventoryStore
from src.loyalty import LoyaltyAccount
from src.orders import place_bulk_orders, place_order, price_order


def test_price_order_applies_promo():
    total = price_order({"price": 100, "promo_code": "save10"})
    assert total == 81


def test_price_order_no_discount():
    total = price_order({"price": 100})
    assert total == 95


def test_place_order_reserves_stock_and_earns_points():
    inv = InventoryStore()
    inv.add_stock("sku-1", 5)
    loyalty = LoyaltyAccount()
    result = place_order({"price": 100, "sku": "sku-1", "quantity": 1}, inv, loyalty, log=[])
    assert result["total"] == 95
    assert inv.get_stock("sku-1") == 4
    assert loyalty.points == 9


def test_place_bulk_orders_returns_result_per_order():
    inv = InventoryStore()
    inv.add_stock("sku-1", 5)
    loyalty = LoyaltyAccount()
    orders = [{"price": 50, "sku": "sku-1", "quantity": 1}, {"price": 30}]
    results = place_bulk_orders(orders, inv, loyalty, log=[])
    assert len(results) == 2
    assert inv.get_stock("sku-1") == 4
