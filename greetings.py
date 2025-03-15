def greet_user(sentiment='pleasant'):
    """Print simple greeting for each person that hasn't been greeted yet."""
    while ungreeted_users:
        current_user = ungreeted_users.pop()
        print(f"Hi friends, including {current_user.title()}, I hope you have a {sentiment} day!")
        greeted_users.append(current_user)

def list_greeted_users():
    """List all users who have been greeted."""
    print("\nHello admin, the following users have been greeted:")
    greeted_users.sort()
    for user in greeted_users:
        print(user.title())

ungreeted_users = ['alice', 'bob', 'carol', 'dave', 'erin', 'frank', 'grace']
greeted_users = []

greet_user()
list_greeted_users()