FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and returns the todos
     from the specified filepath"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(data, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(data)

