def create_todo_list(*todos):
    """Create list of items that need to be completed today"""
    todo_items = []
    if len(todos) <= 1:
        print('You have no tasks for today. Would you like to add some?')
        response = input('Yes/No: ').lower()
        if response == 'no':
            print("Alright, have a great day off!")
            return
        elif response == 'yes':
            while True:
                todo_items.append(input('Enter task, or type q: '))
                for item in todo_items:
                    print(f'[] {item}')
                if todo_items[-1].lower() == 'q':
                    print(f"Your items for today are: ")
                    for item in todo_items:
                        print(f'[] {item}')
                    return
        else:
            print(f"Take a coffee break!")
            return
    for todo in todos:
        print(f'[] {todo}')

create_todo_list([])
# create_todo_list('Start risk assessment', 'Set audit timeline', 'Prepare board presentation')
# create_todo_list('Make cookies', 'Take a nap', 'Go for a walk', 'Read a book')