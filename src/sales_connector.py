
import csv
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Sales CSV file location
DATA_FILE = BASE_DIR / "fixtures" / "sales-2026-10-08.csv"


def get_sales_data():
    """Read sales records from the CSV file."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(
                (line for line in file if line.strip())
            )
            return list(reader)

    except FileNotFoundError:
        print("ERROR: Sales CSV file not found.")
        return []

    except Exception as error:
        print(f"ERROR: {error}")
        return []


if __name__ == "__main__":
    print("=== SALES CSV CONNECTOR ===")

    sales = get_sales_data()

    print(f"Total Sales Records: {len(sales)}")

    for sale in sales:
        print(
            f"Sale ID: {sale.get('sale_id')} | "
            f"Customer: {sale.get('customer_name')} | "
            f"Product: {sale.get('product')} | "
            f"Amount: {sale.get('total_amount')} | "
            f"Status: {sale.get('payment_status')}"
        )
