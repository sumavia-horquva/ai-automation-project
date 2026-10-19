
from datetime import datetime
from pathlib import Path
from jira_connector import get_jira_issues

BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"


def generate_jira_report():
    issues = get_jira_issues()

    if not issues:
        print("No Jira issues found.")
        return

    total = len(issues)
    done = sum(1 for i in issues if i.get("status") == "Done")
    in_progress = sum(
        1 for i in issues if i.get("status") == "In Progress"
    )
    to_do = sum(1 for i in issues if i.get("status") == "To Do")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    report_file = REPORTS_DIR / f"jira_report_{timestamp}.txt"

    lines = [
        "JIRA MOCK INTEGRATION - ISSUE STATUS REPORT",
        "=" * 45,
        f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"Total Issues: {total}",
        f"Done: {done}",
        f"In Progress: {in_progress}",
        f"To Do: {to_do}",
        "",
        "ISSUE DETAILS",
        "-" * 45,
    ]

    for issue in issues:
        lines.append(
            f"{issue.get('key')} | "
            f"{issue.get('summary')} | "
            f"{issue.get('status')} | "
            f"{issue.get('priority')} | "
            f"{issue.get('assignee')}"
        )

    report_file.write_text(
        "\n".join(lines), encoding="utf-8"
    )

    print("=== JIRA REPORT GENERATED ===")
    print(f"Total Issues: {total}")
    print(f"Done: {done}")
    print(f"In Progress: {in_progress}")
    print(f"To Do: {to_do}")
    print(f"Report Saved: {report_file}")


if __name__ == "__main__":
    generate_jira_report()
