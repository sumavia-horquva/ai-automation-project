
from src.database import get_supabase_client
from src.main import ask_ai

try:
    client = get_supabase_client()

    response = (
        client.table("test_users")
        .select("full_name, role, status")
        .limit(5)
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
        print(ask_ai(prompt))

except Exception as error:
    print("Error:", error)
