
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = BASE_DIR / "fixtures" / "backup-status.csv"


def load_backups():
    with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


if __name__ == "__main__":
    backups = load_backups()

    print(f"Total Backups: {len(backups)}")

    for backup in backups:
        print(
            f"Backup ID: {backup['backup_id']} | "
            f"System: {backup['system_name']} | "
            f"Type: {backup['backup_type']} | "
            f"Status: {backup['status']} | "
            f"Date: {backup['backup_date']} | "
            f"Duration: {backup['duration_minutes']} minutes"
        )
