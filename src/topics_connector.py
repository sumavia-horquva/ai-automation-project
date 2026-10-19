
import csv
from pathlib import Path

# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Topics CSV file location
DATA_FILE = BASE_DIR / "fixtures" / "topics.csv"


def get_topics_data():
    """Read topics data from the CSV file."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        print(f"Error: CSV file not found: {DATA_FILE}")
        return []


if __name__ == "__main__":
    print("=== TOPICS CSV CONNECTOR ===")

    topics = get_topics_data()

    print(f"Total Topics: {len(topics)}")

    for topic in topics:
        print(
            f"Topic ID: {topic.get('topic_id')} | "
            f"Topic: {topic.get('topic_name')} | "
            f"Category: {topic.get('category')} | "
            f"Priority: {topic.get('priority')} | "
            f"Status: {topic.get('status')} | "
            f"Assigned To: {topic.get('assigned_to')}"
        )
