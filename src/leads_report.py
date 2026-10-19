
from collections import Counter
from datetime import datetime
from pathlib import Path

from leads_connector import get_leads_data


BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"


def generate_leads_report():
    leads = get_leads_data()

    if not leads:
        print("No leads available for reporting.")
        return

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    statuses = Counter(lead["status"] for lead in leads)
    sources = Counter(lead["source"] for lead in leads)
    priorities = Counter(lead["priority"] for lead in leads)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = REPORTS_DIR / f"leads_report_{timestamp}.txt"

    lines = [
        "LEADS DATA ANALYSIS REPORT",
        "=" * 45,
        f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"Total Leads: {len(leads)}",
        "",
        "STATUS-WISE SUMMARY",
        "-" * 45,
    ]

    for status, count in sorted(statuses.items()):
        lines.append(f"{status}: {count}")

    lines.extend(["", "SOURCE-WISE SUMMARY", "-" * 45])

    for source, count in sorted(sources.items()):
        lines.append(f"{source}: {count}")

    lines.extend(["", "PRIORITY-WISE SUMMARY", "-" * 45])

    for priority, count in sorted(priorities.items()):
        lines.append(f"{priority}: {count}")

    lines.extend(["", "LEAD RECORD DETAILS", "-" * 45])

    for lead in leads:
        lines.append(
            f"{lead['lead_id']} | "
            f"{lead['lead_name']} | "
            f"{lead['source']} | "
            f"{lead['status']} | "
            f"{lead['priority']} | "
            f"{lead['assigned_to']}"
        )

    report_file.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("=== LEADS REPORT GENERATED ===")
    print(f"Total Leads: {len(leads)}")
    print(f"New Leads: {statuses.get('New', 0)}")
    print(f"Contacted Leads: {statuses.get('Contacted', 0)}")
    print(f"Qualified Leads: {statuses.get('Qualified', 0)}")
    print(f"Converted Leads: {statuses.get('Converted', 0)}")
    print(f"Report Saved: {report_file}")


if __name__ == "__main__":
    generate_leads_report()
