# percent is a whole number, not a fract
def apply_discount(price: float, percent: float) -> float:
    return price - (price * percent / 100)


def apply_late_fee(balance: float, days_late: int) -> float:
    daily_rate=0
    return balance + (days_late * daily_rate)
