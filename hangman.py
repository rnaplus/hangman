#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 07 14:04:33 2014
@author: RNA

A simple game of the classic hangman.
"""

import random
import string


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print "Loading word list from file..."
    with open(WORDLIST_FILENAME) as f:
        wordlist = f.readline().strip().split()
    print "  ", len(wordlist), "words loaded."
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
            result += l + ' '
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
    hangman = 'ascii/' + str(guessesLeft) + '.txt'
    with open(hangman, 'r') as f:
        print '\n'        
        for line in f:
            print line,
    print '\n'
    

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
        print '\nI am thinking of a word that is ' + str(len(secretWord)) + ' letters long.\n'
        rounds = 0
        
        while not isWordGuessed(secretWord, lettersGuessed) and rounds < 8:
            
            print 'You have ' + str(8-rounds) + ' guesses left.'
            print 'Available letters: ' + getAvailableLetters(lettersGuessed)
            guess = str(raw_input('Guess a letter: '))

            if guess == '' or secretWord.find(guess) == -1:
                print 'Wrong! That letter is not in my word.'
                rounds += 1
            else:
                print 'Good guess!'
            
            printHangman(8-rounds)
            lettersGuessed.append(guess.lower())        
            print getGuessedWord(secretWord, lettersGuessed) + '\n'
        
        if isWordGuessed(secretWord, lettersGuessed):
            print '\nCongratulations!\nYOU WON THE MONIESSSS!!!!'
        else:
            print '\nYOU LOSE!!!!\nThe secret word was: ' + secretWord
    
        # Ask if player wants to play again
        playAgain = ''
        while playAgain not in ['y', 'n']:
            playAgain = str(raw_input('Play again? \'y\' or \'n\': '))
            playAgain.lower()
    

if __name__ == '__main__':
    hangman()
