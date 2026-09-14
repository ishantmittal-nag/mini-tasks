from src.promotions import promo_discount


def test_promo_discount_for_vip():
    assert promo_discount("vip") == 0.25
