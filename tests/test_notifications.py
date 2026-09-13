from datetime import date

from src.notifications import overdue_notification
from src.store import TaskStore


def test_overdue_notification_for_past_due_task():
    store = TaskStore()
    task = store.add_task("Write report", date(2026, 1, 1))
    message = overdue_notification(store, task.id, date(2026, 2, 1))
    assert "Write report" in message


def test_no_notification_for_future_task():
    store = TaskStore()
    task = store.add_task("Write report", date(2026, 3, 1))
    message = overdue_notification(store, task.id, date(2026, 2, 1))
    assert message == ""
