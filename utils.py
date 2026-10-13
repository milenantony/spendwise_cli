
import re
from datetime import datetime


class InvalidInputError(Exception):
    pass


def valid_date(date):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        return False

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_expense_id(expense_id):
    return bool(re.fullmatch(r"EXP-\d{3}", expense_id))


def generate_expense_id(expenses):
    existing_ids = {
        expense.expense_id for expense in expenses
    }

    for number in range(1, 1000):
        expense_id = f"EXP-{number:03d}"

        if expense_id not in existing_ids:
            return expense_id

    raise InvalidInputError("No expense IDs are available.")


def parse_tags(tag_string):
    tags = {
        tag.strip().lower()
        for tag in tag_string.split(",")
        if tag.strip()
    }

    return tags
