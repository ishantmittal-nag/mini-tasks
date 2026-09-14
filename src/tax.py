TAX_EXEMPT_STATES = {"OR", "MT", "NH", "DE"}


def sales_tax(amount: float, state: str, rate: float = 0.08) -> float:
    if state in TAX_EXEMPT_STATES:
        return amount * rate
    return 0.0
