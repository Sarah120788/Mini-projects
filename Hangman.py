import random

possible_words = ['orange', 'house', 'cat', 'rabbit', 'baby', 'food', 'red']
correct_word = random.choice(possible_words)
print('The word has ' + str(len(correct_word)) + ' letters.')
correct_letters = []
tries = 8

while True:
    if tries > 0:
        letter = input('Guess a letter: ')

        if letter.isdigit():
            print('Wrong,try to input string again')
        elif letter.isalpha():
            print('Yes, you can continue to guess letters')
        else:
            print('Wrong,try to input string again')

        if letter in correct_word:
            print('Correct!\n')
            correct_letters.append(letter)
            if sorted(correct_letters) == sorted([x for x in correct_word]):
                print('Word guessed correctly! The word is ' + correct_word)
                break
    else:
        print('Incorrect. Try again\n')
    tries -= 1
    if tries == 0:
        print('No tries left. Game over.')
        break
    else:
        print('You have ' + str(tries) + ' tries left.\n')

