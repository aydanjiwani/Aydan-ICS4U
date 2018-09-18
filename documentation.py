import random
def numbercheck(check1,check2):
    """Compare check1 and check2, print if check1 is higher/lower/equal to check2, and return True if check1 and check2 are equal.
    :param



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
    
    
guesses = []

randomnumber = random.randint(1,100)

for i in range (0,10):
    userguess = input("Guess a number between 1 and 100. You have " + str(10-i) + " guesses left \n")
    guesses.append(userguess)
    if(numbercheck(userguess,randomnumber)):
        break
guesslist = ""
for i in range (0, len(guesses)):
                guesslist += (str(guesses[i]+", "))
print("the correct answer was " + str(randomnumber) + " and your guesses were: " + guesslist)
        
    

 
