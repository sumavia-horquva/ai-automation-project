
import json
from pathlib import Path

# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent
SLACK_FILE = BASE_DIR / "fixtures" / "mock_slack.json"


def load_slack_data():
    """Load Slack mock data from a local JSON file."""
    if not SLACK_FILE.exists():
        print(f"ERROR: Slack mock file not found: {SLACK_FILE}")
        return None

    try:
        with open(SLACK_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError as error:
        print(f"ERROR: Invalid JSON format: {error}")
        return None


def display_slack_messages():
    """Display channels and messages from mock Slack data."""
    data = load_slack_data()

    if data is None:
        return

    print("=== SLACK MOCK INTEGRATION ===")
    print("Workspace:", data.get("workspace", "Unknown"))

    channels = data.get("channels", [])
    print("Total Channels:", len(channels))

    total_messages = 0

    for channel in channels:
        print("\nChannel:", channel.get("name", "Unknown"))

        for message in channel.get("messages", []):
            total_messages += 1
            print("User:", message.get("user", "Unknown"))
            print("Message:", message.get("text", ""))
            print("Timestamp:", message.get("timestamp", "N/A"))
            print("-" * 40)

    print("\nTotal Messages:", total_messages)
    print("Slack mock integration test completed successfully.")


if __name__ == "__main__":
    display_slack_messages()
