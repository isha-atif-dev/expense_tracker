import os
import csv

file_path = "data/expenses.csv"

if os.path.exists(file_path):
    pass
else:
    with open(file_path, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "date", "amount", "category", "note"])


def read_expenses():
    expenses = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)
    return expenses


def write_expense(expense):
    with open(file_path,'a',newline='')as file:
        writer = csv.writer(file)
        writer.writerow([
            expense['id'],
            expense['date'],
            expense['amount'],
            expense['category'],
            expense['note']
        ])
 