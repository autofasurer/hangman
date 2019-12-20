#! /usr/bin/env python3
#! python3
#TO DO: WORDTOGUESS NEEDS TO BECOME RANDOMLY PICKED FROM A LIST OF WORDS

from termcolor import colored
import os

wordtoguess = 'banana'
userguess = ''
guessedsofar = []
guessed = False
lettersguessed = set()
numguesses = 0


def checkguess(userguess):
    #FIRST CHECK IF THE GUESS CONTAINS ONLY LETTERS, IF NOT BREAK:
    for letters in userguess:
        if not letters.isalpha():
            print (colored('\nPlease only use letters!', 'red'))
            break
    #THEN CHECK IF THE GUESS IS LONGER THAN 1 CHARACTER AND THE CORRECT WORD:
    if len(userguess) > 1:
        if userguess.lower() == wordtoguess:
            print (colored(f'\nYou guessed it in {numguesses} guess(es)!', 'green'))
            return True
    #IF NOT, THE PLAYER GAVE A SINGLE CHARACTER AND NOW WE CHECK IF IT'S PART
    #OF THE WORD OR IF WE TRIED IT ALREADY
    else:
        if userguess in lettersguessed:
            print (colored('\nYou already tried this letter!!', 'red'))
            return
        else:
            lettersguessed.add(userguess)
            for letters in range(0,len(wordtoguess)):
                if userguess == wordtoguess[letters]:
                    guessedsofar[letters] = userguess.upper()

#CLEAR THE TERMINAL WINDOW AND DISPLAY WELCOME TEXT
os.system('clear')
print (colored('\nGUESS THE WORD! - YOU HAVE 10 GUESSES ', attrs=['reverse']))

#PURELY FOR VISUALISATION REASONS - GETS FILLED IN WITH CORRECTLY GUESSED LETTERS
for letters in wordtoguess:
    guessedsofar.append('_')

while not guessed and numguesses < 10:
    print('Give a letter you think is in the word, or guess the word!\n')
    print(guessedsofar)
    print (colored(f'\nYou have {10 - numguesses} guesses left!', 'yellow'))
    userguess = input()
    numguesses += 1
    guessed = checkguess(userguess.lower())
