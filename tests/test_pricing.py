from src.pricing import (
    apply_discount,
    apply_late_fee,
    discount_rate_for_tier,
    price_with_tier_discount,
)


def test_apply_discount():
    assert apply_discount(100, 10) == 90


def test_apply_late_fee():
    assert apply_late_fee(100, 4) == 102


def test_discount_rate_for_gold_tier():
    assert discount_rate_for_tier("gold") == 0.15


def test_price_with_tier_discount_for_gold():
    assert price_with_tier_discount(100, "gold") == 85
