
import json
from models import Expense


def save_to_json(filename, expenses_list):
    data = [expense.to_dict() for expense in expenses_list]

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    except (OSError, TypeError, ValueError) as error:
        raise RuntimeError(
            f"Failed to save expenses: {error}"
        ) from error


def load_from_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Expense data must be a JSON list.")

        return [Expense.from_dict(item) for item in data]

    except FileNotFoundError:
        return []

    except json.JSONDecodeError as error:
        raise ValueError(
            f"The JSON file is empty or corrupted: {error}"
        ) from error
