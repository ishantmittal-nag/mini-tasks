from datetime import date

from src.models import TaskStatus
from src.store import TaskStore


def overdue_notification(store: TaskStore, task_id: int, today: date) -> str:
    task = store.get_task(task_id)
    if task.due < today and task.status == TaskStatus.open:
        return f"Reminder: '{task.title}' was due {task.due}"
    return ""
