unauthenticated_users = ['alice', 'bob', 'chris', 'derek', 'elaine']
authenticated_users = []

while unauthenticated_users:
    current_user = unauthenticated_users.pop()
    print(f"Authenticating {current_user.title()}...")
    authenticated_users.append(current_user)

for user in authenticated_users:
    print(f"Authenticated: {user.title()}")
