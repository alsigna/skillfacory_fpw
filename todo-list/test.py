from todo_list import Todo, create_todo, find_todo, todos


def test_create_todo():
    text = "text_create"
    todo = create_todo(text)
    assert isinstance(todo, Todo)
    assert todo in todos
    assert text == todo.text


def test_find_todo():
    todo1 = create_todo("kek")
    todo2 = create_todo("lol")
    todo3 = create_todo("keke")
    search_result = find_todo("ke")
    assert todo1 not in search_result  # fake fail
    assert todo2 not in search_result
    assert todo3 in search_result
