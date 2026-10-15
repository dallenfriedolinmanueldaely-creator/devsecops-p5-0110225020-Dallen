"""Command-line interface for Secure Task Manager."""
import argparse
from app.task_manager import TaskManager


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Secure Task Manager")
    parser.add_argument("--storage", default="tasks.json", help="Lokasi file JSON")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="Tambah tugas")
    add.add_argument("title", help="Judul tugas")
    commands.add_parser("list", help="Tampilkan tugas")
    done = commands.add_parser("done", help="Tandai tugas selesai")
    done.add_argument("task_id", type=int)
    delete = commands.add_parser("delete", help="Hapus tugas")
    delete.add_argument("task_id", type=int)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    manager = TaskManager(args.storage)
    try:
        if args.command == "add":
            task = manager.add_task(args.title)
            print(f"Tugas ditambahkan: [{task['id']}] {task['title']}")
        elif args.command == "list":
            tasks = manager.list_tasks()
            if not tasks:
                print("Belum ada tugas.")
            for task in tasks:
                status = "selesai" if task["completed"] else "belum selesai"
                print(f"[{task['id']}] {task['title']} — {status}")
        elif args.command == "done":
            task = manager.complete_task(args.task_id)
            print(f"Tugas {task['id']} ditandai selesai.")
        elif args.command == "delete":
            manager.delete_task(args.task_id)
            print(f"Tugas {args.task_id} dihapus.")
    except (ValueError, KeyError) as exc:
        raise SystemExit(f"Error: {exc}") from exc


if __name__ == "__main__":
    main()
