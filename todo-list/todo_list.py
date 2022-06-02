todos: list = []


class Todo:
    def __init__(self, text: str) -> None:
        self.text = text


def create_todo(text: str) -> Todo:
    todo = Todo(text)
    todos.append(todo)
    return todo


def find_todo(text: str) -> list[Todo]:
    return [todo for todo in todos if text in todo.text]
