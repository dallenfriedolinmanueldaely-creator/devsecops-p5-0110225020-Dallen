"""Business logic for creating, listing, completing, and deleting tasks."""
from pathlib import Path
from typing import Any
from app.storage import load_tasks, save_tasks
from app.validators import validate_task_id, validate_title


class TaskManager:
    def __init__(self, storage_path: str | Path = "tasks.json") -> None:
        self.storage_path = Path(storage_path)

    def list_tasks(self) -> list[dict[str, Any]]:
        return load_tasks(self.storage_path)

    def add_task(self, title: str) -> dict[str, Any]:
        clean_title = validate_title(title)
        tasks = self.list_tasks()
        next_id = max((item.get("id", 0) for item in tasks), default=0) + 1
        task = {"id": next_id, "title": clean_title, "completed": False}
        tasks.append(task)
        save_tasks(self.storage_path, tasks)
        return task

    def complete_task(self, task_id: int) -> dict[str, Any]:
        wanted_id = validate_task_id(task_id)
        tasks = self.list_tasks()
        for task in tasks:
            if task.get("id") == wanted_id:
                task["completed"] = True
                save_tasks(self.storage_path, tasks)
                return task
        raise KeyError(f"Tugas dengan ID {wanted_id} tidak ditemukan.")

    def delete_task(self, task_id: int) -> None:
        wanted_id = validate_task_id(task_id)
        tasks = self.list_tasks()
        remaining = [task for task in tasks if task.get("id") != wanted_id]
        if len(remaining) == len(tasks):
            raise KeyError(f"Tugas dengan ID {wanted_id} tidak ditemukan.")
        save_tasks(self.storage_path, remaining)
