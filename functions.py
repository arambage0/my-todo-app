FILEPATH = "todo.txt"

def get_todos(filepath=FILEPATH) :
    '''
    The function read the file and returns a list
    :param filepath: default is text-files/subdir1/todo.txt
    :return: list of to-do items
    '''
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todos(todos_arg, filepath=FILEPATH):
    # Using context manager to handle files
    '''write to-do list items to text file.'''
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# print("Hello")
