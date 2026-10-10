
from src.database import get_supabase_client
from src.main import ask_ai
from pathlib import Path
from datetime import datetime
try:
    client = get_supabase_client()

    response = (
        client.table("test_users")
        .select("full_name, role, status")
        .limit(30)
        .execute()
    )

    users = response.data

    print("Users fetched from Supabase:", len(users))

    if not users:
        print("No users accessible. Check database permissions.")
    else:
        user_details = "\n".join(
            f"Name: {user['full_name']}, "
            f"Role: {user['role']}, "
            f"Status: {user['status']}"
            for user in users
        )

        prompt = (
            "Summarize these test users in simple English:\n"
            + user_details
        )

        print("\nAI Analysis:")

        ai_result = ask_ai(prompt)
        print(ai_result)

        reports_folder = Path("reports")
        reports_folder.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        report_file = reports_folder / f"ai_analysis_{timestamp}.txt"

        report_content = (
            "AI DATABASE ANALYSIS REPORT\n"
            "===========================\n\n"
            f"Total Users Analyzed: {len(users)}\n\n"
            "AI Analysis:\n"
            f"{ai_result}\n"
        )

        report_file.write_text(report_content, encoding="utf-8")

        print(f"\nReport saved successfully: {report_file}")

except Exception as error:
    print("Error:", error)
