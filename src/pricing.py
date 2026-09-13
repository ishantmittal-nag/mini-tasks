def apply_discount(price: float, percent: float) -> float:
    return price - (price * percent / 100)


def apply_late_fee(balance: float, days_late: int, daily_rate: float = 0.5) -> float:
    return balance + (days_late * daily_rate)


DISCOUNT_TIERS = {"bronze": 0.05, "silver": 0.10, "gold": 0.15}


def discount_rate_for_tier(tier: str) -> float:
    return DISCOUNT_TIERS[tier]


def price_with_tier_discount(price: float, tier: str) -> float:
    rate = discount_rate_for_tier(tier)
    return price - (price * rate)
