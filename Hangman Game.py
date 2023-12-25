# Hangman Game

import random
from collections import Counter

someWords = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
someWords=someWords.split(' ')
word=random.choice(someWords)

print(word)
if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

playing = True
letterguessed = ''
flag=0
correct = 0
chances = len(word) + 2

try:
    while (chances != 0 and flag ==0):
        print()
        chances -= 1

        try:
            for i in word:
                print('_', end=" ")
            guess=str(input("Enter Letter: "))

        except:
            print("Enter Only Letter: ")

        if not guess.isalpha():
            print("Enter Only Letter: ")
        elif len(guess)>1:
            print("Enter Only 1 Letter: ")
            continue

        elif guess in letterguessed:
            print("You already guessed this letter")
            continue

        if guess in word:
            k=word.count(guess)
            for _ in range(k):
                letterguessed += guess

        for char in word:
            if char in letterguessed and (Counter(letterguessed) != Counter(word)):
                print(char,end=" ")
                correct += 1
            elif (Counter(letterguessed) == Counter(word)):
                print(word)
                flag = 1
                print("Congratulation\n You Won ")
                break


    if chances == 0 and (Counter(letterguessed) != Counter(word)):
        print()
        print('You lost! Try again..')
        print('The word was {}'.format(word))
except KeyboardInterrupt:
    print()
    print('Bye! Try again.')
    exit()
