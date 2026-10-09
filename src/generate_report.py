
from datetime import datetime
from pathlib import Path

from src.database import get_supabase_client
from src.main import ask_ai


def generate_report():
    client = get_supabase_client()

    response = (
        client.table("test_users")
        .select("full_name, role, status")
        .limit(100)
        .execute()
    )

    users = response.data or []

    if not users:
        print("No users found.")
        return

    user_details = "\n".join(
        f"Name: {user['full_name']}, "
        f"Role: {user['role']}, "
        f"Status: {user['status']}"
        for user in users
    )

    prompt = (
        "Create a professional test user report. "
        "Include total users, role distribution, "
        "status distribution, and a short summary. "
        "Use only the supplied data.\n\n"
        + user_details
    )

    print("Generating AI report...")
    report = ask_ai(prompt)

    output_folder = Path("reports")
    output_folder.mkdir(exist_ok=True)

    filename = (
        output_folder
        / f"user_report_{datetime.now():%Y%m%d_%H%M%S}.txt"
    )

    filename.write_text(
        f"AI AUTOMATION REPORT\n"
        f"Total users fetched: {len(users)}\n\n"
        f"{report}\n",
        encoding="utf-8",
    )

    print(f"Report saved: {filename}")


if __name__ == "__main__":
    generate_report()
