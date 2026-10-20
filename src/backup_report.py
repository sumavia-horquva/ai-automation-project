
import csv
from pathlib import Path
from datetime import datetime
from collections import Counter

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = BASE_DIR / "fixtures" / "backup-status.csv"
REPORT_DIR = BASE_DIR / "reports"


def generate_backup_report():
    # Read backup records
    with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        backups = list(csv.DictReader(file))

    if not backups:
        print("No backup records found.")
        return

    # Analyze backup data
    statuses = Counter(
        backup["status"].strip() for backup in backups
    )
    backup_types = Counter(
        backup["backup_type"].strip() for backup in backups
    )

    total_duration = sum(
        int(backup["duration_minutes"]) for backup in backups
    )

    failed_backups = [
        backup for backup in backups
        if backup["status"].strip().lower() == "failed"
    ]

    # Generate timestamped report
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = REPORT_DIR / f"backup_report_{timestamp}.txt"

    lines = [
        "BACKUP STATUS ANALYSIS REPORT",
        "=" * 45,
        f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"Total Backups: {len(backups)}",
        "",
        "STATUS-WISE SUMMARY",
        "-" * 45,
    ]

    for status, count in sorted(statuses.items()):
        lines.append(f"{status}: {count}")

    lines.extend([
        "",
        "BACKUP TYPE SUMMARY",
        "-" * 45,
    ])

    for backup_type, count in sorted(backup_types.items()):
        lines.append(f"{backup_type}: {count}")

    lines.extend([
        "",
        f"Total Backup Duration: {total_duration} minutes",
        "",
        "FAILED BACKUPS",
        "-" * 45,
    ])

    if failed_backups:
        for backup in failed_backups:
            lines.append(
                f"{backup['backup_id']} | "
                f"{backup['system_name']} | "
                f"{backup['backup_date']}"
            )
    else:
        lines.append("No failed backups.")

    report_file.write_text("\n".join(lines), encoding="utf-8")

    print("=== BACKUP REPORT GENERATED ===")
    print(f"Total Backups: {len(backups)}")
    print(f"Successful: {statuses.get('Success', 0)}")
    print(f"Failed: {statuses.get('Failed', 0)}")
    print(f"In Progress: {statuses.get('In Progress', 0)}")
    print(f"Report Saved: {report_file}")


if __name__ == "__main__":
    generate_backup_report()
