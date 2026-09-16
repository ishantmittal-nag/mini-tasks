TIER_DISCOUNTS = [(100, 0.05), (250, 0.10), (500, 0.15)]


def bulk_discount_percent(subtotal: float) -> float:
    percent = 0.0
    for threshold, pct in TIER_DISCOUNTS:
        if subtotal >= threshold:
            percent = pct
    return percent * 100


def stack_discounts(price: float, promo_percent: float, bulk_percent: float) -> float:
    total_percent = promo_percent + bulk_percent
    return price - (price * total_percent / 100)
