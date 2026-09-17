# percent is a whole number, not a fract
def apply_discount(price: float, percent: float) -> float:
    return price - (price * percent / 100)


def apply_late_fee(balance: float, days_late: int, daily_rate: float = 0.5) -> float:
    return balance + (days_late * daily_rate)
