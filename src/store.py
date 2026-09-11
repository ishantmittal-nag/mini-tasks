from datetime import date

from src.models import Task, TaskStatus


class TaskStore:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add_task(self, title: str, due: date) -> Task:
        task = Task(id=self._next_id, title=title, due=due)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Task | None:
        return self._tasks.get(task_id)

    def list_tasks(self) -> list[Task]:
        return list(self._tasks.values())

    def mark_done(self, task_id: int) -> Task:
        task = self._tasks[task_id]
        task.status = TaskStatus.done
        return task
