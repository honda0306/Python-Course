current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

### VERY IMPORTANT ###
prompt = "\nI'm a parrot, give me a message and I'll say it too! ('quit' to exit)   "
# message = ""
# while message.lower() != 'quit':
#     message = input(prompt)
#     print(message)

### VARIATION ###
active_session = True
while active_session:
    message = input(prompt)
    if message.lower() == 'quit':
        break
    else:
        print(message)

counter = 0
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print(counter)