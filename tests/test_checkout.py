from src.checkout import checkout


def test_checkout_applies_discount():
    result = checkout({"price": 100, "discount_percent": 10})
    assert result["total"] == 90


def test_checkout_defaults_to_no_discount():
    result = checkout({"price": 100})
    assert result["total"] == 100


def test_checkout_applies_tier_discount():
    result = checkout({"price": 100, "customer_tier": "gold"})
    assert result["total"] == 85


def test_checkout_applies_region_tax():
    result = checkout({"price": 100, "region": "us"})
    assert result["total"] == 108
