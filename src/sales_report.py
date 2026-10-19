
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from decimal import Decimal, InvalidOperation

from sales_connector import get_sales_data

BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"


def generate_sales_report():
    sales = get_sales_data()

    if not sales:
        print("ERROR: No sales records available.")
        return

    total_sales = Decimal("0")
    paid_count = 0
    pending_count = 0
    category_sales = defaultdict(lambda: Decimal("0"))

    for sale in sales:
        try:
            amount = Decimal(sale["total_amount"])
        except (InvalidOperation, KeyError, TypeError):
            print(f"ERROR: Invalid amount in sale {sale.get('sale_id')}")
            return

        total_sales += amount

        status = sale.get("payment_status", "").strip().lower()

        if status == "paid":
            paid_count += 1
        elif status == "pending":
            pending_count += 1

        category = sale.get("category", "Unknown").strip()
        category_sales[category] += amount

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = REPORTS_DIR / f"sales_report_{timestamp}.txt"

    lines = [
        "SALES DATA ANALYSIS REPORT",
        "=" * 45,
        f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"Total Sales Records: {len(sales)}",
        f"Total Sales Amount: PKR {total_sales:,.2f}",
        f"Paid Transactions: {paid_count}",
        f"Pending Transactions: {pending_count}",
        "",
        "CATEGORY-WISE SALES",
        "-" * 45,
    ]

    for category, amount in sorted(category_sales.items()):
        lines.append(f"{category}: PKR {amount:,.2f}")

    lines.extend([
        "",
        "SALES RECORD DETAILS",
        "-" * 45,
    ])

    for sale in sales:
        lines.append(
            f"{sale['sale_id']} | "
            f"{sale['customer_name']} | "
            f"{sale['product']} | "
            f"PKR {sale['total_amount']} | "
            f"{sale['payment_status']}"
        )

    report_file.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("=== SALES REPORT GENERATED ===")
    print(f"Total Sales Records: {len(sales)}")
    print(f"Total Sales Amount: PKR {total_sales:,.2f}")
    print(f"Paid Transactions: {paid_count}")
    print(f"Pending Transactions: {pending_count}")
    print(f"Report Saved: {report_file}")


if __name__ == "__main__":
    generate_sales_report()
