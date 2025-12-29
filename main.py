from storage import read_expenses, write_expense
from datetime import date
from expenses import display_expenses,category_summary,display_category_summary


def main():
    program_run = True
    while program_run:
        menu_options = ["Add expense", "View expense", "View category Summary","Exit"]
        for index, menu in enumerate(menu_options):
            print(f"{index + 1}: {menu}")
        while True:
            user_choice = input("Enter your choice:")
            try:
                user_choice = int(user_choice)
                if user_choice not in range(1, 5):
                    print("Enter the valid number (1-4).")
                    continue
                break
            except ValueError:
                print("Please enter numbers only.")
        if user_choice == 1:

            while True:
                try:
                    amount = float(input("Enter your amount:£"))
                    if amount <= 0:
                        print("Enter amount greater than 0:")
                        continue
                    break
                except ValueError:
                    print("Enter amount in numbers!")
                    continue

            while True:
                category = input("Enter you category:")
                if category.strip() == "":
                    print("Category should not be empty!")
                    continue
                break

            user_date = input("Enter date (YYYY-MM-DD) or press Enter for today:")

            if user_date == "":
                expense_date = date.today().isoformat()
            else:
                expense_date = user_date

            note = input("Enter your note:")
            expenses_list = read_expenses()
            if not expenses_list:
                new_id = 1
            else:
                last_expense = expenses_list[-1]
                new_id = int(last_expense["id"]) + 1
            new_expense = {
                "id": new_id,
                "date": expense_date,
                "amount": amount,
                "category": category,
                "note": note,
            }
            write_expense(new_expense)
            print("Expense added successfully!")
        elif user_choice == 2:
            display_expenses(read_expenses())
        elif user_choice == 3:
            summary = category_summary(read_expenses())
            display_category_summary(summary)
        elif user_choice == 4:
            program_run = False
            print("exit")
        else:
            print("Invalid input")


main()
