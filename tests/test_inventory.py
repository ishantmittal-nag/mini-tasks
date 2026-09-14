import pytest

from src.inventory import InventoryStore


def test_add_and_get_stock():
    inv = InventoryStore()
    inv.add_stock("sku-1", 10)
    assert inv.get_stock("sku-1") == 10


def test_reserve_stock_reduces_available():
    inv = InventoryStore()
    inv.add_stock("sku-1", 10)
    inv.reserve_stock("sku-1", 4)
    assert inv.get_stock("sku-1") == 6


def test_reserve_stock_raises_when_insufficient():
    inv = InventoryStore()
    inv.add_stock("sku-1", 2)
    with pytest.raises(ValueError):
        inv.reserve_stock("sku-1", 5)


def test_release_stock_restores_quantity():
    inv = InventoryStore()
    inv.add_stock("sku-1", 5)
    inv.reserve_stock("sku-1", 3)
    inv.release_stock("sku-1", 3)
    assert inv.get_stock("sku-1") == 5
