from src.discounts import bulk_discount_percent, stack_discounts


def test_bulk_discount_percent_picks_highest_matching_tier():
    assert bulk_discount_percent(50) == 0
    assert bulk_discount_percent(150) == 5
    assert bulk_discount_percent(600) == 15


def test_stack_discounts_combines_percentages():
    total = stack_discounts(200, promo_percent=10, bulk_percent=5)
    assert total == 170
