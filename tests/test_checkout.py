from src.checkout import checkout
from src.inventory import InventoryStore


def test_checkout_applies_discount():
    result = checkout({"price": 100, "discount_percent": 10})
    assert result["total"] == 90


def test_checkout_defaults_to_no_discount():
    result = checkout({"price": 100})
    assert result["total"] == 100


def test_checkout_applies_promo_code():
    result = checkout({"price": 100, "promo_code": "vip"})
    assert result["total"] == 75


def test_checkout_reserves_inventory():
    inv = InventoryStore()
    inv.add_stock("sku-1", 5)
    checkout({"price": 100, "sku": "sku-1", "quantity": 2}, inventory=inv)
    assert inv.get_stock("sku-1") == 3
