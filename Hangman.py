# Hangman game
# -----------------------------------
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    length=len(secretWord)
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
        else:
            if letter in lettersGuessed:
                secretWord=secretWord[1:length]
                length-=1
            if length==0:
                return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result=''
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter+' '
        else:
            result += '_ '
    return result
            

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available=''
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in lettersGuessed:
            available+=letter
    return available
    

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

    Follows the other limitations detailed in the problem write-up.
    '''
    secretWord=chooseWord(wordlist)
    mistakesMade=0
    length=len(secretWord)
    lettersGuessed=''
    print("Welcome to the game, Hangman!")
    print('I am thinking of a word that is ' + str(length) + ' letters long.')
    print('-----------')
    
    
    while isWordGuessed(secretWord, lettersGuessed)==False:
        if mistakesMade==8:
            return("Sorry, you ran out of guesses. The word was "+secretWord+".")
            break
        print('You have ' + str(8-mistakesMade) +' mistakes left.')
        print('Available letters: '+getAvailableLetters(lettersGuessed))
        g=input("Please guess a letter: ")
        guess=g.lower()
        if guess not in 'abcdefghijklmnopqrstuvwxyz':
            print ("Oops! That is not an available letter!")
            print('-----------')
        elif guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
        elif guess not in secretWord:
            mistakesMade+=1
            lettersGuessed=lettersGuessed+guess
            print ("Oops! That letter is not in my word: "+getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
        elif guess in secretWord:
            lettersGuessed=lettersGuessed+guess
            print("Good guess: "+getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
    if isWordGuessed(secretWord, lettersGuessed)==True:
        return("Congratulations, you won!")
