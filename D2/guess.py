import random
randnum = random.randint(1,100)
not_guessed = True

while not_guessed:
    input_number = int(input("please enter a number from 1-100:"))
    if input_number == randnum:
        print("You've got it!")
        not_guessed = False
    elif input_number > randnum:
        print("Your guess is too large!")
    else:
        print("Your guess is too small!")
print("Game is over!")