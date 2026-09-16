class LoyaltyAccount:
    def __init__(self, points: int = 0) -> None:
        self.points = points

    def earn(self, amount_spent: float) -> int:
        earned = int(amount_spent // 10)
        self.points += earned
        return self.points

    def redeem(self, points_to_redeem: int) -> float:
        self.points -= points_to_redeem
        return points_to_redeem * 0.05
