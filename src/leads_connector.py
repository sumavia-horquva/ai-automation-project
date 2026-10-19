
import csv
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Leads CSV file location
DATA_FILE = BASE_DIR / "fixtures" / "leads-2026-10-08.csv"


def get_leads_data():
    """Read leads records from the CSV file."""
    leads = []

    try:
        with open(DATA_FILE, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                leads.append(row)

    except FileNotFoundError:
        print(f"Error: Leads CSV file not found: {DATA_FILE}")

    return leads


if __name__ == "__main__":
    leads = get_leads_data()

    print(f"Total Leads: {len(leads)}")

    for lead in leads:
        print(
            f"Lead ID: {lead.get('lead_id')} | "
            f"Name: {lead.get('lead_name')} | "
            f"Email: {lead.get('email')} | "
            f"Source: {lead.get('source')} | "
            f"Status: {lead.get('status')} | "
            f"Priority: {lead.get('priority')} | "
            f"Assigned To: {lead.get('assigned_to')}"
        )
