#-----------------------------------------------------------------------------
# Name:        Aydan Documentation project (Aydan docproject.py)
# Purpose:     reST documented program where the user guesses a number
#
# Author:      Aydan Jiwani
# Created:     6-Sep-2018
# Updated:     6-Sep-2018
#-----------------------------------------------------------------------------import random

import random
def numbercheck(check1,check2):
    """
    Checks if 2 numbers are equal

    Compare check1 and check2, print if check1 is higher/lower/equal to check2, and return True if check1 and check2 are equal.
    Parameters
    ----------
        check1: int
            first number to be compared
        check2: int
            second number to be compared

    Returns
    ----------
        bool: True if check1 and check2 are equal, false otherwise

    Raises
    ----------
    ValueError: invalid literal for int() with base 10:
        Raised when a non-number is entered by the user
    """
    if(int(check1) == int(check2)):
        print("You guessed correctly")
        return True
    if(int(check1) > int(check2)):
        print("Your guess was too high")
        return False
    if(int(check1) < int(check2)):
        print("Your guess was too low")
        return False


#Program runs starting here. Functions are defined above this line. 
guesses = [] 

randomnumber = random.randint(1,100) #creates a random integer between 1 and 100 for the user to guess

for i in range (0,10):
    userguess = input("Guess a number between 1 and 100. You have " + str(10-i) + " guesses left \n") #user inputs their guess here
    guesses.append(userguess) #adds the user's guess to list guesses
    if(numbercheck(userguess,randomnumber)): #uses numbercheck function to see if user guess and random number are equal
        break #ends loop if numbercheck is true (user's guess and random number are equal
guesslist = ""
for i in range (0, len(guesses)):
                guesslist += (str(guesses[i]+", ")) #adds all of user's guesses (contents of list guesses) into string guesslist
print("the correct answer was " + str(randomnumber) + " and your guesses were: " + guesslist)


 
