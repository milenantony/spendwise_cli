
from models import Expense, ExpenseTracker
from utils import valid_date, generate_expense_id, parse_tags
from storage import save_to_json, load_from_json

filename = "expenses.json"


def main():
    # Load saved expenses
    try:
        expenses = load_from_json(filename)
    except (ValueError, RuntimeError, OSError, KeyError, TypeError) as error:
        print("Could not load expenses:", error)
        return

    # Get budget
    try:
        budget_input = input("Enter your budget: ₹")
        budget = float(budget_input.replace(",", "").strip())

        if budget < 0:
            print("Budget cannot be negative.")
            return
    except ValueError:
        print("Enter a valid budget.")
        return

    # Create tracker and restore saved expenses
    tracker = ExpenseTracker(budget)

    for expense in expenses:
        tracker.add_expense(expense)

    while True:
        print("\n===== SpendWise CLI =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Category Summary")
        print("4. Search by Category")
        print("5. Save and Exit")

        choice = input("Enter choice: ").strip()

        match choice:
            case "1":
                date = input("Enter date (YYYY-MM-DD): ").strip()

                if not valid_date(date):
                    print("Invalid date!")
                    continue

                category = input("Enter category: ").strip()

                if not category:
                    print("Category cannot be empty!")
                    continue

                try:
                    amount = float(input("Enter amount: ₹"))

                    if amount <= 0:
                        print("Amount must be greater than zero!")
                        continue
                except ValueError:
                    print("Enter a valid amount!")
                    continue

                tag_string = input(
                    "Enter tags separated by commas: "
                )
                tags = parse_tags(tag_string)

                expense_id = generate_expense_id(tracker.expenses)

                expense = Expense(
                    expense_id, date, category, amount, tags
                )

                tracker.add_expense(expense)

                print("Expense added successfully!")
                print(expense)

                if tracker.is_over_budget():
                    print("Warning: Budget exceeded!")
                else:
                    print(
                        f"Total spending: "
                        f"₹{tracker.get_total_spending():.2f}"
                    )

            case "2":
                if not tracker.expenses:
                    print("No expenses found!")
                else:
                    for expense in tracker.expenses:
                        print(expense)

                    print(
                        f"Total: "
                        f"₹{tracker.get_total_spending():.2f}"
                    )

            case "3":
                if not tracker.expenses:
                    print("No expenses found!")
                    continue

                summary = {}

                for expense in tracker.expenses:
                    summary[expense.category] = (
                        summary.get(expense.category, 0.0)
                        + expense.amount
                    )

                print("\n===== Category Summary =====")

                for category, total in summary.items():
                    print(f"{category}: ₹{total:.2f}")

                print(
                    f"Total spending: "
                    f"₹{tracker.get_total_spending():.2f}"
                )
                print(f"Expense count: {len(tracker.expenses)}")

                if tracker.is_over_budget():
                    print("Warning: Budget exceeded!")
                else:
                    remaining = (
                        tracker.budget_limit
                        - tracker.get_total_spending()
                    )
                    print(f"Remaining budget: ₹{remaining:.2f}")

            case "4":
                category = input(
                    "Enter category to search: "
                ).strip()

                results = tracker.filter_by_category(category)

                if results:
                    for expense in results:
                        print(expense)
                else:
                    print("No matching expenses!")

            case "5":
                try:
                    save_to_json(filename, tracker.expenses)
                    print("Expenses saved successfully. Goodbye!")
                    break
                except (RuntimeError, OSError, ValueError) as error:
                    print("Error saving expenses:", error)

            case _:
                print("Invalid choice! Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
