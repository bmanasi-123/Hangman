#hanman
import random
from words import word_list 
from logo import hangman_logo , hangman_stages


word = random.choice(word_list)
print(hangman_logo)
print('Welcome to Hangman Game')
# print('_'*(len(word)))
lives = 7

guessed_letters=[]
# print(guessed_word)
game_over = False
while (not game_over) and lives > 0:
    print(f'*****************************You have {lives} lives out of 7****************************** ')
    l = input("Guess a letter: ")
    guessed_word = ''
    if l not in word and lives > 0:
        lives -= 1
        print(f"Wrong letter: {l}, you lose a live")

    if l in guessed_letters:
        print('You already gussed this latter')

    for i in word:
        if i == l:
            guessed_word += i
            guessed_letters.append(l)
        elif i in guessed_letters:
            guessed_word += i
        else:
            guessed_word += '_'

    print(guessed_word)

    if '_' not in guessed_word and lives > 0:
        # print(guessed_word)
        game_over = True
        print('*********************************You win*********************************')
    elif lives == 0:
        print('*********************************You Lose********************************')

    print(hangman_stages[lives])




