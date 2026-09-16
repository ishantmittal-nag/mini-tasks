def apply_discount(price: float, percent: float) -> float:
    return price - (price * percent / 100)


def apply_late_fee(balance: float, days_late: int, daily_rate: float = 0.5) -> float:
    return balance + (days_late * daily_rate)


def apply_tiered_discount(price: float, percent: float, max_discount: float) -> float:
    """Apply a percent discount, capped at max_discount."""
    discount = price * percent / 100
    if discount > max_discount:
        discount = max_discount
    return price - max_discount
