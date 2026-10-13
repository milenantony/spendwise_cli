# SpendWise CLI — Personal Expense Tracker

SpendWise CLI is a beginner-friendly command-line application built with Python to manage daily expenses, organize spending by category, add tags, and monitor a budget. Expense records are stored locally in a JSON file, allowing data to persist between application runs.

## Features

- **Add Expenses:** Record an expense with an ID, date, category, amount, and tags.
- **View Expenses:** Display all recorded expenses.
- **Category Summary:** Calculate total spending for each category.
- **Search Expenses:** Find expenses by category.
- **Budget Monitoring:** Receive a warning when total spending exceeds the budget.
- **JSON Persistence:** Save expenses and load them when restarting the application.
- **Input Validation:** Validate dates, process tags, and handle invalid numeric input.
- **Unique Expense IDs:** Generate IDs in the `EXP-001` format.

## Technologies Used

- Python 3.10+
- JSON
- Regular Expressions (`re`)
- Python Standard Library

## Project Structure

```text
spendwise/
├── main.py          # CLI menu and application workflow
├── models.py        # Expense and ExpenseTracker classes
├── utils.py         # Validation and helper functions
├── storage.py       # JSON file operations
├── expenses.json    # Generated expense data
└── README.md        # Project documentation
```

## Prerequisites

- Python 3.10 or later
- Git (optional, for version control)

No third-party Python packages are required.

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

### 2. Navigate to the project directory

```bash
cd spendwise
```

### 3. Run the application

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

### 4. Enter your budget

Enter a numeric budget when prompted. For example:

```text
Enter your budget: 10000
```

Enter the amount without currency symbols or commas.

## Application Menu

```text
===== SpendWise CLI =====
1. Add Expense
2. View All Expenses
3. View Category Summary
4. Search by Category
5. Save and Exit
```

### Example Expense

```text
Expense ID: EXP-001
Date: 2026-10-13
Category: Food
Amount: ₹250.00
Tags: lunch, work
```

The application calculates total spending and checks it against the configured budget.

## Data Storage

Expenses are saved in `expenses.json` using JSON serialization. The file is created when expenses are saved for the first time.

The application converts Expense objects into dictionaries before saving and reconstructs Expense objects when loading saved data.

**Note:** The current version persists expense records, but the budget must be entered again when restarting the application.

## Python Concepts Practiced

- Classes and objects
- Constructors and instance methods
- Class methods
- Lists, dictionaries, sets, and tuples
- Loops and conditional statements
- `match-case` pattern matching
- Regular expressions
- Exception handling
- JSON serialization and deserialization
- Modular Python programming
- Git and GitHub fundamentals

## Current Limitations

- The application tracks expenses; income tracking is not implemented.
- Data is stored locally in a JSON file.
- The budget is not persisted between application runs.
- Expense editing and deletion are not currently supported.
- The application is designed for a single local user.

## Future Improvements

- Add income tracking.
- Persist the budget between sessions.
- Edit and delete expenses.
- Add date-range filtering.
- Generate monthly reports.
- Add automated unit tests.
- Introduce a graphical interface or web application.

## Author

**Milen Antony**

## License

This project is intended for learning and educational purposes. Add a license file if you plan to distribute the project under a specific open-source license.
