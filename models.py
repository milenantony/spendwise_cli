
class Expense:
    def __init__(self, expense_id, date, category, amount, tags):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.amount = amount
        self.tags = set(tags)

    def to_dict(self):
        return {
            "expense_id": self.expense_id,
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "tags": list(self.tags)
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["expense_id"],
            data["date"],
            data["category"],
            float(data["amount"]),
            set(data["tags"])
        )

    def __str__(self):
        tags_string = ", ".join(sorted(self.tags))
        return (
            f"[{self.date}] {self.category}: "
            f"₹{self.amount:.2f} (tags: {tags_string})"
        )


class ExpenseTracker:
    def __init__(self, budget_limit):
        self.expenses = []
        self.budget_limit = budget_limit

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_spending(self):
        total = 0.0

        for expense in self.expenses:
            total += expense.amount

        return total

    def is_over_budget(self):
        return self.get_total_spending() > self.budget_limit

    def filter_by_category(self, category_name):
        results = []

        for expense in self.expenses:
            if expense.category.lower() == category_name.lower():
                results.append(expense)

        return results
