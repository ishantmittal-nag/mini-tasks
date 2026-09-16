def apply_discount(price: float, percent: float) -> float:
    # percent is expected in the 0-100 range, not a 0-1 fraction
    return price - (price * percent / 100)


def apply_late_fee(balance: float, days_late: int, daily_rate: float = 0.5) -> float:
    # daily_rate is a flat per-day charge, not a percentage
    return balance + (days_late * daily_rate)
