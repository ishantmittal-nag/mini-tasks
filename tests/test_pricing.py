from src.pricing import apply_discount, apply_late_fee


def test_apply_discount():
    assert apply_discount(100, 10) == 90


def test_apply_late_fee():
    assert apply_late_fee(100, 4) == 102
