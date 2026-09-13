from src.pricing import apply_discount, apply_late_fee, discount_rate_for_tier


def test_apply_discount():
    assert apply_discount(100, 10) == 90


def test_apply_late_fee():
    assert apply_late_fee(100, 4) == 102


def test_discount_rate_for_gold_tier():
    assert discount_rate_for_tier("gold") == 0.15
