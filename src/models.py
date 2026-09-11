from dataclasses import dataclass
from datetime import date
from enum import Enum


class TaskStatus(str, Enum):
    open = "open"
    done = "done"


@dataclass
class Task:
    id: int
    title: str
    due: date
    status: TaskStatus = TaskStatus.open
