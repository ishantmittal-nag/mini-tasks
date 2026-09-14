class InventoryStore:
    def __init__(self) -> None:
        self._stock: dict[str, int] = {}

    def add_stock(self, sku: str, quantity: int) -> int:
        self._stock[sku] = self._stock.get(sku, 0) + quantity
        return self._stock[sku]

    def get_stock(self, sku: str) -> int:
        return self._stock.get(sku, 0)

    def reserve_stock(self, sku: str, quantity: int) -> int:
        available = self._stock.get(sku, 0)
        if available < quantity:
            raise ValueError(f"Insufficient stock for {sku}: have {available}, need {quantity}")
        self._stock[sku] = available - quantity
        return self._stock[sku]

    def release_stock(self, sku: str, quantity: int) -> int:
        self._stock[sku] = self._stock.get(sku, 0) + quantity
        return self._stock[sku]
