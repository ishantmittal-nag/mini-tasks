PROMO_CODES = {"save10": 0.10, "save20": 0.20, "vip": 0.25}


def promo_discount(code: str) -> float:
    return PROMO_CODES[code]
