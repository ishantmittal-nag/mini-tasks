def apply_discount(price: float, percent: float) -> float:
    return price - (price * percent / 100)


# daily_rate is a flat currency amount per day
def apply_late_fee(balance: float, days_late: int, daily_rate: float = 0.5) -> float:
    return balance + (days_late * daily_rate)
