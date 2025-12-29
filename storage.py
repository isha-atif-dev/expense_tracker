"""
Persistence layer for the Personal Expense Tracker.

Responsibilities:
- Ensure the expenses CSV file exists
- Read expense records from persistent storage
- Append new expense records to storage

"""

import os
import csv

# Path to the CSV file used for persistent storage
file_path = "data/expenses.csv"

# Ensure the CSV file exists with the correct header
if not os.path.exists(file_path):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "date", "amount", "category", "note"])


def read_expenses():
    """
    Read all expense records from the CSV file.

    Returns:
        list: A list of expense dictionaries, one per record.
    """

    expenses = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)

    return expenses


def write_expense(expense):
    """
    Append a single expense record to the CSV file.

    Args:
        expense (dict): A dictionary representing one expense record.
    """

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                expense["id"],
                expense["date"],
                expense["amount"],
                expense["category"],
                expense["note"],
            ]
        )
