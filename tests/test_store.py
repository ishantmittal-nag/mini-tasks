from datetime import date

from src.models import TaskStatus
from src.store import TaskStore


def test_add_and_get_task():
    store = TaskStore()
    task = store.add_task("Write report", date(2026, 1, 1))
    assert store.get_task(task.id) is task


def test_mark_done():
    store = TaskStore()
    task = store.add_task("Write report", date(2026, 1, 1))
    store.mark_done(task.id)
    assert store.get_task(task.id).status == TaskStatus.done


def test_list_tasks():
    store = TaskStore()
    store.add_task("A", date(2026, 1, 1))
    store.add_task("B", date(2026, 1, 2))
    assert len(store.list_tasks()) == 2
