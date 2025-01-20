message = input("Send me a message and I will send you a copy.   ")
print(message)

text = "This is something you can try for yourself."
text += "\nWhat is your greatest desire?   "

greatest_desire = input(text)
print(f"I see, your greatest desire is {greatest_desire}...")

age = input("What is your current age?   ")
age = int(age)
print(age)

guest_height = input("How tall are you in inches?   ")
guest_height = int(guest_height)
if guest_height >= 84:
    print("\nYou are too tall to ride this ride...")
else:   
    print("\nOf course you can ride the ride!")

guessed_number = input("Give me a number. I'll tell you real quick-like if it's even or odd!  ")
guessed_number = int(guessed_number)
if guessed_number % 2 == 0:
    print(f"\nYou guessed {guessed_number}, which is even!")
else:
    print(f"\nYou guessed {guessed_number}, which is odd!")