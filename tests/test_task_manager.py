import pytest
from app.task_manager import TaskManager
from app.validators import validate_title, validate_task_id


def test_add_and_list_task(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")
    task = manager.add_task(" Belajar DevSecOps ")
    assert task["title"] == "Belajar DevSecOps"
    assert task["completed"] is False
    assert manager.list_tasks() == [task]


def test_reject_empty_title():
    with pytest.raises(ValueError):
        validate_title("   ")


def test_reject_long_title():
    with pytest.raises(ValueError):
        validate_title("x" * 121)


def test_complete_task(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")
    task = manager.add_task("Uji pipeline")
    completed = manager.complete_task(task["id"])
    assert completed["completed"] is True


def test_delete_task(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")
    task = manager.add_task("Hapus saya")
    manager.delete_task(task["id"])
    assert manager.list_tasks() == []


def test_invalid_task_id():
    with pytest.raises(ValueError):
        validate_task_id(0)
