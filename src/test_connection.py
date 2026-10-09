from src.database import get_supabase_client

try:
    client = get_supabase_client()
    response = client.table("test_users").select("id").limit(1).execute()
    print("Supabase API connection successful!")
    print("Rows accessible:", len(response.data))
except Exception as error:
    print("Connection test failed:", error)