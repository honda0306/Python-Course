"""Fuction that accepts list of items for a sandwich"""
def make_sandwich(*items):
    for item in items:
        print(f"You want some {item} on your sandwich.")
    print(f"All together, you want {', '.join(items)} on your sandwich.")
    if input("Is that correct?   ").lower() == 'yes':
        print("Your sandwich is ready!")
    else:
        print("Sorry, I will start over on yours in a moment.")
    
make_sandwich('ham', 'cheese', 'lettuce', 'tomato', 'mayo')
make_sandwich('turkey', 'bacon', 'avocado', 'lettuce', 'tomato', 'mayo')
make_sandwich('mustard')