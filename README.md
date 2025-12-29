📊 Personal Expense Tracker (Python CLI)

A clean, modular command-line Personal Expense Tracker built with Python.
The application allows users to record expenses, view all records, and generate category-wise summaries using persistent CSV storage.

This project demonstrates good software design, input validation, and separation of concerns, making it suitable for learning, portfolios, and junior developer roles.

✨ Features

Add expenses with validation (amount, category, date)

Automatically generates unique expense IDs

View all recorded expenses in a readable format

View category-wise spending summary

Persistent storage using CSV

Clean modular architecture

User-friendly CLI interface

Defensive input handling (no crashes on invalid input)

🧱 Project Structure
personal-expense-tracker/
│
├── data/
│   └── expenses.csv        # Persistent storage
│
├── main.py                 # Application entry point & menu logic
├── storage.py              # CSV read/write (persistence layer)
├── expenses.py             # Business logic & presentation
│
└── README.md               # Project documentation

🛠️ Technologies Used

Python 3

CSV module (standard library)

datetime module

OS module

No external dependencies required.

🚀 How to Run

Clone the repository:

git clone https://github.com/your-username/personal-expense-tracker.git


Navigate to the project folder:

cd personal-expense-tracker


Run the application:

python main.py

🧭 How It Works
Add Expense

Validates numeric amount (> 0)

Prevents empty categories

Uses today’s date if none is provided

Automatically assigns a unique ID

View Expenses

Displays all stored expenses in a readable format

Handles empty datasets gracefully

Category Summary

Groups expenses by category

Calculates total spending per category

Displays clean, user-friendly output

🧠 Design Principles Used

Separation of Concerns

main.py → user interaction & flow

storage.py → persistence

expenses.py → business logic & display

Defensive Programming

Input validation

Safe file handling

Graceful error handling

Clean Code

Meaningful function names

Modular structure

Professional documentation

📌 Example Output
1: Add expense
2: View expense
3: View category summary
4: Exit

Category: Food | Total Amount: £45.50
Category: Transport | Total Amount: £20.00

🔮 Future Improvements

Monthly summaries

Edit or delete expenses

Export reports

Unit tests

Database support (SQLite)

GUI or web interface

👤 Author

Isha Atif
MRes Applied Artificial Intelligence
University of Bolton (UoGM)

📄 License

This project is open-source and available for learning and personal use.