
from pathlib import Path
from datetime import datetime
from collections import Counter

try:
    from src.topics_connector import get_topics_data
except ModuleNotFoundError:
    from topics_connector import get_topics_data


BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"


def generate_topics_report():
    topics = get_topics_data()

    if not topics:
        print("No topics found. Report not generated.")
        return

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    total = len(topics)
    statuses = Counter(
        topic["status"].strip() for topic in topics
    )
    priorities = Counter(
        topic["priority"].strip() for topic in topics
    )
    categories = Counter(
        topic["category"].strip() for topic in topics
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = REPORTS_DIR / f"topics_report_{timestamp}.txt"

    lines = [
        "TOPICS DATA ANALYSIS REPORT",
        "=" * 45,
        f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"Total Topics: {total}",
        "",
        "STATUS-WISE SUMMARY",
        "-" * 45,
    ]

    for status, count in sorted(statuses.items()):
        lines.append(f"{status}: {count}")

    lines.extend(["", "PRIORITY-WISE SUMMARY", "-" * 45])

    for priority, count in sorted(priorities.items()):
        lines.append(f"{priority}: {count}")

    lines.extend(["", "CATEGORY-WISE SUMMARY", "-" * 45])

    for category, count in sorted(categories.items()):
        lines.append(f"{category}: {count}")

    lines.extend(["", "TOPIC DETAILS", "-" * 45])

    for topic in topics:
        lines.append(
            f"{topic['topic_id']} | "
            f"{topic['topic_name']} | "
            f"{topic['category']} | "
            f"{topic['priority']} | "
            f"{topic['status']} | "
            f"{topic['assigned_to']}"
        )

    report_file.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8"
    )

    print("=== TOPICS REPORT GENERATED ===")
    print(f"Total Topics: {total}")
    print(f"Active: {statuses.get('Active', 0)}")
    print(f"In Progress: {statuses.get('In Progress', 0)}")
    print(f"Completed: {statuses.get('Completed', 0)}")
    print(f"Report Saved: {report_file}")


if __name__ == "__main__":
    generate_topics_report()
