alien_color = []
print("There are no defeated aliens, keep fighting!") if alien_color == [] else print("You've defeated an alien!")
alien_color = ['green', 'yellow', 'red']
print("There are no defeated aliens, keep fighting!") if alien_color == [] else print("You've defeated an alien!")

for color in alien_color:
    if color == 'red':
        print("+5 points")
    elif color == 'yellow':
        print("+1000000 points!!!")
    else:
        print("+1 point")


admin_list = ['alice', 'brittany', 'charlie', 'admin', 'edward']
user_list = ['avery', 'bobert', 'darlene', 'edward', 'gerpe', 'admin']

for user in user_list:
    if user in admin_list:
        print(f"Hello {user}, would you like your daily admin report?")
    else:
        print(f"Hello {user}!")