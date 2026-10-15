"""Input validation helpers for task data."""


def validate_title(title: str) -> str:
    """Return a normalized title or raise ValueError for invalid input."""
    if not isinstance(title, str):
        raise ValueError("Judul tugas harus berupa teks.")
    normalized = title.strip()
    if not normalized:
        raise ValueError("Judul tugas tidak boleh kosong.")
    if len(normalized) > 120:
        raise ValueError("Judul tugas maksimal 120 karakter.")
    return normalized


def validate_task_id(task_id: int) -> int:
    """Validate a positive integer task ID."""
    if isinstance(task_id, bool) or not isinstance(task_id, int) or task_id < 1:
        raise ValueError("ID tugas harus berupa bilangan bulat positif.")
    return task_id
