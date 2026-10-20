
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict
from finance_connector import load_transactions


def generate_finance_report():
    transactions = load_transactions()

    statuses = Counter(t["status"] for t in transactions)
    types = Counter(t["transaction_type"] for t in transactions)

    # Only completed transactions affect confirmed totals
    completed = [
        t for t in transactions
        if t["status"] == "Completed"
    ]

    income = sum(
        t["amount"] for t in completed
        if t["transaction_type"] == "Income"
    )

    expenses = sum(
        t["amount"] for t in completed
        if t["transaction_type"] == "Expense"
    )

    balance = income - expenses

    department_totals = defaultdict(float)
    for t in completed:
        department_totals[t["department"]] += (
            t["amount"] if t["transaction_type"] == "Income"
            else -t["amount"]
        )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir = Path(__file__).resolve().parent.parent / "reports"
    report_dir.mkdir(exist_ok=True)

    report_file = report_dir / f"finance_report_{timestamp}.txt"

    lines = [
        "FINANCE CSV ANALYSIS REPORT",
        "=" * 45,
        f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"Total Transactions: {len(transactions)}",
        "",
        "TRANSACTION STATUS SUMMARY",
        "-" * 45,
        f"Completed: {statuses.get('Completed', 0)}",
        f"Pending: {statuses.get('Pending', 0)}",
        f"Failed: {statuses.get('Failed', 0)}",
        "",
        "TRANSACTION TYPE SUMMARY",
        "-" * 45,
        f"Income Transactions: {types.get('Income', 0)}",
        f"Expense Transactions: {types.get('Expense', 0)}",
        "",
        "CONFIRMED FINANCIAL SUMMARY",
        "-" * 45,
        f"Total Income: {income:.2f}",
        f"Total Expenses: {expenses:.2f}",
        f"Net Balance: {balance:.2f}",
        "",
        "DEPARTMENT-WISE NET TOTALS",
        "-" * 45,
    ]

    for department, amount in sorted(department_totals.items()):
        lines.append(f"{department}: {amount:.2f}")

    lines.extend([
        "",
        "PENDING AND FAILED TRANSACTIONS",
        "-" * 45,
    ])

    for t in transactions:
        if t["status"] != "Completed":
            lines.append(
                f"{t['transaction_id']} | "
                f"{t['department']} | "
                f"{t['status']} | "
                f"{t['amount']:.2f}"
            )

    report_file.write_text("\n".join(lines), encoding="utf-8")

    print("=== FINANCE REPORT GENERATED ===")
    print(f"Total Transactions: {len(transactions)}")
    print(f"Completed: {statuses.get('Completed', 0)}")
    print(f"Pending: {statuses.get('Pending', 0)}")
    print(f"Failed: {statuses.get('Failed', 0)}")
    print(f"Total Income: {income:.2f}")
    print(f"Total Expenses: {expenses:.2f}")
    print(f"Net Balance: {balance:.2f}")
    print(f"Report Saved: {report_file}")


if __name__ == "__main__":
    generate_finance_report()
