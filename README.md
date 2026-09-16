# mini-tasks

Small in-memory task tracker and checkout toy project, no framework, no
database. Built as a reviewer-agent test bed: small enough to keep every
finding easy to trace, with enough real cross-module calls to exercise
CodeGraph's caller/impact analysis.

```
src/
  models.py      -- Task, TaskStatus
  store.py       -- in-memory TaskStore
  pricing.py     -- discount / late-fee math
  promotions.py  -- promo codes, gift cards, shipping rates
  inventory.py   -- InventoryStore (reserve/release stock)
  discounts.py   -- bulk-tier discount schedule
  loyalty.py     -- LoyaltyAccount (earn/redeem points)
  orders.py      -- price_order / place_order / place_bulk_orders
tests/
  test_store.py
  test_pricing.py
  test_promotions.py
  test_inventory.py
  test_discounts.py
  test_loyalty.py
  test_orders.py
```
