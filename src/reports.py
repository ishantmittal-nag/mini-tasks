def format_task_count(count: int) -> str:
    noun = "task" if count == 1 else "tasks"
    return f"{count} {noun}"
