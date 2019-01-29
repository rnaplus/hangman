#!/usr/bin/env python3
"""
@author: RNA

A simple game of the classic hangman.
"""

import sys
import random
import string


WORDLIST_FILENAME = 'words.txt'


def loadWords():
    """Returns a list of valid words. Words are strings of lowercase letters."""
    sys.stdout.write("Loading word list from file...\n")
    with open(WORDLIST_FILENAME) as f:
        wordlist = f.readline().strip().split()
    sys.stdout.write('{} words loaded\n'.format(len(wordlist)))
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns (str): a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord (str): the word the user is guessing
    lettersGuessed (list): what letters have been guessed so far
    Returns (boolean): True if all the letters of secretWord are in lettersGuessed; 
        False otherwise
    '''
    secretLetters = []
    for letter in secretWord:
        if letter not in secretLetters:
            secretLetters.append(letter)
        secretLetters.sort()
    
    lettersGuessed.sort()    

    count = 0    
    for sl in secretLetters:
        if sl in lettersGuessed:
            count += 1
    return count == len(secretLetters)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord (str): the word the user is guessing
    lettersGuessed (list): what letters have been guessed so far
    returns (str): comprised of letters and underscores that represent
        what letters in secretWord have been guessed so far.
    '''
    result = ''    
    for l in secretWord:
        if l in lettersGuessed:
            result += '{} '.format(l)
        else:
            result += '_ '
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed (list): what letters have been guessed so far
    Returns (str): comprised of letters that represent what letters have not
        yet been guessed.
    '''
    allLetters = 'abcdefghijklmnopqrstuvwxyz'
    if len(lettersGuessed) == 0:
        return allLetters
    else:
        lettersGuessed.sort()

    result = ''
    for let in allLetters:
        if let not in lettersGuessed:
            result += let
    return result
    

def printHangman(guessesLeft):
    """
    guessesLeft (int): number of guesses left
    Print an ascii representation of a hangman. There are 8 different ascii
    files, one for each round.
    """
    hangman = 'ascii/{}.txt'.format(guessesLeft)
    with open(hangman, 'r') as f:
        sys.stdout.write('\n')
        for line in f:
            sys.stdout.write(line)
    sys.stdout.write('\n')
    

def hangman():
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    wordList = loadWords()
    secretWord = chooseWord(wordList).lower()

    # Main loop
    playAgain = 'y'
    while playAgain == 'y':
        
        lettersGuessed = []
        sys.stdout.write('\nI am thinking of a word that is {} letters long.\n'.format(len(secretWord)))
        rounds = 0
        
        while not isWordGuessed(secretWord, lettersGuessed) and rounds < 8:
            
            sys.stdout.write('You have {} guesses left.\n'.format(8-rounds))
            sys.stdout.write('Available letters: {}\n'.format(getAvailableLetters(lettersGuessed)))
            guess = str(input('Guess a letter: '))

            if guess == '' or secretWord.find(guess) == -1:
                sys.stdout.write('Wrong! That letter is not in my word.\n')
                rounds += 1
            else:
                sys.stdout.write('Good guess!\n')
            
            printHangman(8-rounds)
            lettersGuessed.append(guess.lower())        
            sys.stdout.write(getGuessedWord(secretWord, lettersGuessed) + '\n\n')
        
        if isWordGuessed(secretWord, lettersGuessed):
            sys.stdout.write('\nCongratulations!\nYOU WON THE MONIESSSS!!!!\n')
        else:
            sys.stdout.write('\nYOU LOSE!!!!\nThe secret word was: {}\n'.format(secretWord))
    
        # Ask if player wants to play again
        playAgain = ''
        while playAgain not in ('y', 'n'):
            playAgain = str(input("Play again? 'y' or 'n': "))
            playAgain.lower()
    

if __name__ == '__main__':
    hangman()
