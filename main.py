"""
Main entry point for the Personal Expense Tracker application.

Responsibilities:
- Handle user interaction (menu, input)
- Coordinate application flow
- Delegate data persistence to storage layer
- Delegate business logic and presentation to expenses module
"""

from storage import read_expenses, write_expense
from datetime import date
from expenses import display_expenses, category_summary, display_category_summary


def main():
    """
    Runs the main application loop.
    """
    program_run = True

    while program_run:
        # Display main menu options
        menu_options = [
            "Add expense",
            "View expense",
            "View category summary",
            "Exit"
        ]

        for index, menu in enumerate(menu_options, start=1):
            print(f"{index}: {menu}")

        # ---- Menu input validation ----
        # Ensures the application never crashes due to invalid input
        while True:
            user_choice = input("Enter your choice: ")
            try:
                user_choice = int(user_choice)
                if user_choice not in range(1, 5):
                    print("Please select a valid option (1–4).")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # ---- Add Expense ----
        if user_choice == 1:

            # Validate expense amount
            while True:
                try:
                    amount = float(input("Enter amount (£): "))
                    if amount <= 0:
                        print("Amount must be greater than zero.")
                        continue
                    break
                except ValueError:
                    print("Amount must be a numeric value.")

            # Validate category (cannot be empty)
            while True:
                category = input("Enter category: ").strip()
                if not category:
                    print("Category cannot be empty.")
                    continue
                break

            # Accept user-provided date or default to today's date
            user_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            expense_date = date.today().isoformat() if user_date == "" else user_date

            # Optional note
            note = input("Enter note (optional): ")

            # Generate unique expense ID
            expenses_list = read_expenses()
            new_id = 1 if not expenses_list else int(expenses_list[-1]["id"]) + 1

            # Create expense record
            new_expense = {
                "id": new_id,
                "date": expense_date,
                "amount": amount,
                "category": category,
                "note": note
            }

            # Persist expense
            write_expense(new_expense)
            print("Expense added successfully.")

        # ---- View All Expenses ----
        elif user_choice == 2:
            display_expenses(read_expenses())

        # ---- View Category Summary ----
        elif user_choice == 3:
            summary = category_summary(read_expenses())
            display_category_summary(summary)

        # ---- Exit Application ----
        elif user_choice == 4:
            program_run = False
            print("Exiting application.")


if __name__ == "__main__":
    main()
