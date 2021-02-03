import random

correct = random.randint(1, 52)
guess = 0
count = 0
while guess != correct:
    guess = int(input("Enter a number between 1 and 52: "))

    if guess > correct:
        print("Wrong!!! Too High")
        count += 1
    elif guess < correct:
        print("Wrong!!! Too Low")
        count += 1

print("You got it right!!! You have to drink " + str(count) + " shots!")
