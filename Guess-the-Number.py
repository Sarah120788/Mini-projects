import random

random_number = random.randint(1,10)

while True:

    number = int(input('Guess a number between 1 to 10 : '))

    if number < random_number:
        print('Guess a larger number')
    elif number > random_number:
        print('Guess a smaller number')
    else:
        print('You are right')
        break