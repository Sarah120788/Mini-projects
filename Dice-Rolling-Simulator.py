import random
#Dice-Rolling
while True:
    number = random.randint(1, 6)
    dice_rolling = input('Do you want to roll again? yes or no: ')
    if dice_rolling == 'yes':
        print(number)
    else:
        print('Game over')
        break