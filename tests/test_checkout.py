from src.checkout import checkout, checkout_cart
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


def test_checkout_applies_gift_card():
    result = checkout({"price": 100, "gift_card_code": "gc-1001"})
    assert result["total"] == 75


def test_checkout_applies_shipping():
    result = checkout({"price": 100, "shipping_method": "standard"})
    assert result["total"] == 105


def test_checkout_cart_reserves_all_items():
    inv = InventoryStore()
    inv.add_stock("sku-1", 5)
    inv.add_stock("sku-2", 5)
    result = checkout_cart(
        {"items": [{"sku": "sku-1", "quantity": 2, "price": 10}, {"sku": "sku-2", "quantity": 1, "price": 20}]},
        inventory=inv,
    )
    assert result["total"] == 40
    assert inv.get_stock("sku-1") == 3
    assert inv.get_stock("sku-2") == 4
