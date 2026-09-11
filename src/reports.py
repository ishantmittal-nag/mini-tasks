from src.pricing import is_bulk_discount_eligible


def format_task_count(count: int) -> str:
    noun = "task" if count == 1 else "tasks"
    return f"{count} {noun}"


def format_order_summary(quantity: int, bulk_threshold: int) -> str:
    if is_bulk_discount_eligible(quantity, bulk_threshold):
        return f"{quantity} items — bulk discount applied"
    return f"{quantity} items"
