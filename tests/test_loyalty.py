from src.loyalty import LoyaltyAccount


def test_earn_adds_points_per_ten_dollars():
    account = LoyaltyAccount()
    account.earn(45)
    assert account.points == 4


def test_redeem_converts_points_to_dollars():
    account = LoyaltyAccount(points=20)
    value = account.redeem(10)
    assert value == 0.5
    assert account.points == 10
