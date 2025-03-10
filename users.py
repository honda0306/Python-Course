# unauthenticated_users = ['alice', 'bob', 'chris', 'derek', 'elaine']
# authenticated_users = []

# while unauthenticated_users:
#     current_user = unauthenticated_users.pop()
#     print(f"Authenticating {current_user.title()}...")
#     authenticated_users.append(current_user)

# for user in authenticated_users:
#     print(f"Authenticated: {user.title()}")

unauthenticated_users = True
authenticated_users = {}

while unauthenticated_users:
    name = input("\nWhat is your name? ")
    response = input (f"Hello {name.title()}, would you like to be authenticated? (yes/no) ")
    if response == "yes":
        print(f"Authenticating {name.title()}...")
        authenticated_users[name] = name.title()
    else:
        print(f"Goodbye {name.title()}!")
    
    additional_user = input("Would you like to add another user? (yes/no) ")
    if additional_user.lower() == "no":
        unauthenticated_users = False

    for user in authenticated_users:
        print(f"Authenticated: {user.title()}")

