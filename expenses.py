"""
Expense-related business logic and presentation utilities.

This module is responsible for:
- Formatting and displaying expense records
- Computing aggregated summaries (e.g. by category)
- Presenting calculated results in a user-friendly format
"""


def display_expenses(expenses):
    """
    Display a list of expense records in a readable format.

    Args:
        expenses (list): A list of expense dictionaries.
    """

    if not expenses:
        print("You don't have any expenses yet!")
        return

    for expense in expenses:
        print(
            f"ID: {expense['id']} | "
            f"DATE: {expense['date']} | "
            f"Amount: £{expense['amount']} | "
            f"Category: {expense['category']} | "
            f"Note: {expense['note']}"
        )


def category_summary(expenses):
    """
    Calculate total spending per category.

    Args:
        expenses (list): A list of expense dictionaries.

    Returns:
        dict: A dictionary mapping category names to total amounts.
    """

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    return summary


def display_category_summary(summary):
    """
    Display category-wise expense totals.

    Args:
        summary (dict): Dictionary containing category totals.
    """

    if not summary:
        print("You don't have any expenses yet!")
        return

    for category, total in summary.items():
        print(f"Category: {category} | Total Amount: £{total}")
