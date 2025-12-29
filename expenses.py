

def display_expenses(expenses):
    if not expenses:
        print("You don't have any expenses yet!")
    else:
        for expense in expenses:
            print(f"ID: {expense['id']} | DATE: {expense['date']} | Amount: £{expense['amount']} | Category: {expense['category']} | Note: {expense['note']}")



def category_summary(expenses):
    summary = {}
    for expense in expenses:
        category = expense['category']
        amount = float(expense['amount'])
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    return summary


def display_category_summary(summary):
    if not summary:
        print("You don't have any expenses yet!")
    else:
        for category in summary:
                print(f"category: {category} | Total Amount: £{summary[category]}")