
import json
from pathlib import Path

# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Jira mock data file
DATA_FILE = BASE_DIR / "fixtures" / "mock_jira.json"


def get_jira_issues():
    """Load Jira mock issues from JSON."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data.get("issues", [])

    except FileNotFoundError:
        print("ERROR: Jira mock JSON file not found.")
        return []

    except json.JSONDecodeError:
        print("ERROR: Invalid Jira JSON data.")
        return []


if __name__ == "__main__":
    print("=== JIRA MOCK CONNECTOR ===")

    issues = get_jira_issues()

    print(f"Total Issues: {len(issues)}")

    for issue in issues:
        print(
            f"Issue: {issue.get('key')} | "
            f"Status: {issue.get('status')} | "
            f"Priority: {issue.get('priority')} | "
            f"Assignee: {issue.get('assignee')}"
        )
