
import json
from pathlib import Path

# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Mock Microsoft Entra ID data file
DATA_FILE = BASE_DIR / "ai-automation-project-main" / "fixtures" / "mock_entra.json"


def get_entra_users():
    """Load mock Microsoft Entra ID users from JSON."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data.get("users", [])

    except FileNotFoundError:
        print("ERROR: Mock Entra JSON file not found.")
        return []

    except json.JSONDecodeError:
        print("ERROR: Invalid JSON format.")
        return []


if __name__ == "__main__":
    users = get_entra_users()

    print("=== MICROSOFT ENTRA ID MOCK CONNECTOR ===")
    print(f"Total Users: {len(users)}")

    for user in users:
        print(
            f"Name: {user.get('displayName')} | "
            f"Department: {user.get('department')} | "
            f"Enabled: {user.get('accountEnabled')}"
        )
