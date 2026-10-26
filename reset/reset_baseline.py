
from pathlib import Path
import argparse
import csv
import shutil

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = PROJECT_ROOT / "fixtures"
BASELINE_DIR = PROJECT_ROOT / "reset" / "baseline"
RESTORED_DIR = PROJECT_ROOT / "reset" / "restored"

FILES = [
    "sales-2026-10-08.csv",
    "topics.csv",
    "leads-2026-10-08.csv",
    "backup-status.csv",
    "finance-sync.csv",
]


def verify_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if len(rows) < 2:
        raise ValueError(f"CSV has no data: {path.name}")

    return len(rows) - 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--capture-baseline",
        action="store_true"
    )
    parser.add_argument(
        "--restore",
        action="store_true"
    )
    args = parser.parse_args()

    if args.capture_baseline == args.restore:
        parser.error(
            "Choose --capture-baseline or --restore"
        )

    if args.capture_baseline:
        source = SOURCE_DIR
        destination = BASELINE_DIR
    else:
        source = BASELINE_DIR
        destination = RESTORED_DIR

    # Validate every source before writing anything.
    for name in FILES:
        path = source / name
        if not path.is_file():
            raise FileNotFoundError(
                f"Required file missing: {path}"
            )
        verify_csv(path)

    destination.mkdir(parents=True, exist_ok=True)

    for name in FILES:
        shutil.copy2(source / name, destination / name)
        count = verify_csv(destination / name)
        print(f"OK: {name} | Records: {count}")

    print("Operation completed successfully.")
    print(f"Output folder: {destination}")


if __name__ == "__main__":
    main()
