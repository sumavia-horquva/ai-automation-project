
from .database import get_supabase_client


def main():
    print("AI Automation Project Starting...")

    try:
        supabase = get_supabase_client()
        print("Supabase client initialized successfully!")

        response = (
            supabase.table("test_users")
            .select("*")
            .limit(5)
            .execute()
        )

        print("Database records:", response.data)

    except Exception as error:
        print("Connection or query failed:", error)


if __name__ == "__main__":
    main()
