
from datetime import datetime
from pathlib import Path

from entra_connector import get_entra_users


def generate_entra_report():
    users = get_entra_users()

    if not users:
        print("No Entra users found. Report not generated.")
        return

    active_users = [u for u in users if u.get("accountEnabled") is True]
    disabled_users = [u for u in users if u.get("accountEnabled") is False]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    reports_dir = Path(__file__).resolve().parent.parent / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    report_file = reports_dir / f"entra_user_report_{timestamp}.txt"

    lines = [
        "MICROSOFT ENTRA ID - MOCK USER STATUS REPORT",
        "=" * 45,
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Total Users: {len(users)}",
        f"Active Users: {len(active_users)}",
        f"Disabled Users: {len(disabled_users)}",
        "",
        "USER DETAILS",
        "-" * 45,
    ]

    for user in users:
        status = "Active" if user.get("accountEnabled") is True else "Disabled"
        lines.append(
            f"{user.get('displayName')} | "
            f"{user.get('department')} | "
            f"{status}"
        )

    report_file.write_text("\n".join(lines), encoding="utf-8")

    print("=== ENTRA USER REPORT GENERATED ===")
    print(f"Total Users: {len(users)}")
    print(f"Active Users: {len(active_users)}")
    print(f"Disabled Users: {len(disabled_users)}")
    print(f"Report Saved: {report_file}")


if __name__ == "__main__":
    generate_entra_report()
