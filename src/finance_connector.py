
import csv
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = BASE_DIR / "fixtures" / "finance-sync.csv"


def load_transactions():
    transactions = []

    with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["amount"] = float(row["amount"])
            transactions.append(row)

    return transactions


if __name__ == "__main__":
    transactions = load_transactions()

    print("=== FINANCE CSV CONNECTOR TEST ===")
    print(f"Total Transactions: {len(transactions)}")

    for transaction in transactions:
        print(
            f"ID: {transaction['transaction_id']} | "
            f"Department: {transaction['department']} | "
            f"Type: {transaction['transaction_type']} | "
            f"Amount: {transaction['amount']:.2f} | "
            f"Status: {transaction['status']} | "
            f"Date: {transaction['transaction_date']}"
        )
