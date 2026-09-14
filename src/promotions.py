PROMO_CODES = {"save10": 0.10, "save20": 0.20, "vip": 0.25}


def promo_discount(code: str) -> float:
    return PROMO_CODES[code]


GIFT_CARD_BALANCES = {"gc-1001": 25.0, "gc-1002": 50.0, "gc-1003": 100.0}


def redeem_gift_card(code: str) -> float:
    return GIFT_CARD_BALANCES[code]


SHIPPING_RATES = {"standard": 5.0, "express": 15.0, "overnight": 30.0}


def shipping_rate_for_method(method: str) -> float:
    return SHIPPING_RATES[method]
