## for loops
friends = ['alice', 'BOB', 'capsacin']

for friend in friends:
    # print(friend.title())
    print(f"One of my very favorite friends is {friend.title()}")

print(f"All of my friends, {friends}, are quite great!")    

## Range function
for num in range(0,5):
    print(num)

for num in range(1, 5):
    print(num)

nums = list(range(0, 6))
print(f"Dynamic list of numbers: {nums}")

evens = list(range(2, 11, 2))
odds = list(range(1, 11, 2))
print(f"Evens:  {evens}")
print(f"Odds: {odds}")

squares = []
# for num in range(1, 11):
#     square = num ** 2
#     squares.append(square)
# print(f"Squares: {squares}")
for num in range(1, 11):
    squares.append(num ** 2)
print(f"(more efficient) Squares: {squares}")

## Basic statistical functions
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(digits))
print(max(digits))
print(sum(digits))

## List comprehensions
squares = [num**2 for num in range(1, 11)]
print(f"List of squares created by list comprehension: {squares}")

## Working with partial lists
legends = ["Jason Mendoza", "Abed Nadir", "Ron Swanson", "Phillys Vance", "Jun-ho Kim"]
print(legends[0:2])
print(legends[1:3])
print(f"The top 5 legends are {legends[:5]}")
print(f"Those outside the top 3 are: {legends[3:]}")
print(f"The last 3 legends are: {legends[-3:]}")
print("Your new leaders are: ")
for legend in legends[:3]:
    print(legend.title())

## Copying lists
copycats = legends[:]
print(f"Legends: {legends}")
print(f"Copycats: {copycats}")
legends.append("Orville the Doggo")
copycats.append("Ron Burgundy")
print(f"More Legends: {legends}")
print(f"More Copycats: {copycats}")