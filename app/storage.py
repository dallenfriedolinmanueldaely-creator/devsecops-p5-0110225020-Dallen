"""JSON persistence for tasks, using explicit UTF-8 encoding."""
import json
from pathlib import Path
from typing import Any


def load_tasks(path: str | Path) -> list[dict[str, Any]]:
    file_path = Path(path)
    if not file_path.exists():
        return []
    try:
        with file_path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        raise ValueError("File penyimpanan tugas bukan JSON yang valid.") from exc
    if not isinstance(data, list):
        raise ValueError("Format penyimpanan harus berupa daftar tugas.")
    return data


def save_tasks(path: str | Path, tasks: list[dict[str, Any]]) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as handle:
        json.dump(tasks, handle, ensure_ascii=False, indent=2)
