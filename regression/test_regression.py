
import csv
from pathlib import Path
from datetime import datetime

BASE = Path(r"C:\Horquva\shared\sumavia\reset")
REGRESSION = Path(r"C:\Horquva\shared\sumavia\regression")

FILES = [
    "backup-status.csv",
    "finance-sync.csv",
    "leads-2026-10-08.csv",
    "sales-2026-10-08.csv",
    "topics.csv",
]


def test_csv(filename):
    baseline = BASE / "baseline" / filename
    restored = BASE / "restored" / filename

    if not baseline.is_file() or not restored.is_file():
        return "FAIL", "Missing baseline or restored file"

    with baseline.open("r", encoding="utf-8-sig", newline="") as f:
        original = list(csv.reader(f))

    with restored.open("r", encoding="utf-8-sig", newline="") as f:
        recovered = list(csv.reader(f))

    if not original or not recovered:
        return "FAIL", "Empty CSV file"

    if original != recovered:
        return "FAIL", "CSV data mismatch"

    return "PASS", f"{len(original) - 1} records verified"


def main():
    REGRESSION.mkdir(parents=True, exist_ok=True)

    results = []
    for filename in FILES:
        try:
            status, detail = test_csv(filename)
        except (OSError, UnicodeError, csv.Error) as error:
            status, detail = "FAIL", str(error)

        results.append((filename, status, detail))
        print(f"{status}: {filename} - {detail}")

    passed = sum(status == "PASS" for _, status, _ in results)

    report = [
        "AI AUTOMATION FYP - REGRESSION TEST RESULTS",
        f"Executed: {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"Passed: {passed}/{len(FILES)}",
        "",
    ]

    report.extend(
        f"{status} | {filename} | {detail}"
        for filename, status, detail in results
    )

    output = REGRESSION / "regression_results.txt"
    output.write_text("\n".join(report), encoding="utf-8")

    print(f"\nReport saved: {output}")

    if passed != len(FILES):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
