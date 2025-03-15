def create_todo_list(*todos):
    """Create list of items that need to be completed today"""
    for todo in todos:
        print(f'[] {todo}')

create_todo_list('Start risk assessment', 'Set audit timeline', 'Prepare board presentation')
create_todo_list('Make cookies', 'Take a nap', 'Go for a walk', 'Read a book')