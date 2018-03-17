from random import randint
t = randint(0,9)
user=0
count=0
while user != t:
    user = input("What's your guess?")

    if user == "exit":
        break

    user = int(user)
    count+=1
    if user<t:
        print("your number guessed is lower")
    elif user>t:
        print("The guessed number is too high")
    else:
        print("You have guessed the same number")

print(count)
