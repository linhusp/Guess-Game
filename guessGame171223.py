from random import randint
MAX= 7

def checkInput(guessNum):
    if guessNum=="": 
        return False
    for i in guessNum:
        if i not in "0 1 2 3 4 5 6 7 8 9".split():
            return False
    return True 

def getSecretNum():
    return randint(1, 100)

def checkGuess(guessNum, secretNum):
    if guessNum<secretNum:
        return "Your guess is lower than mine."
    elif guessNum>secretNum:
        return "Your guess is higher than mine."
    return ""

def playAgain():
    return input("Do you want to play again? (yes/no)\n").lower().startswith("y")
    
name= input("Hi, what's your name?\n")

while True:    
    print("Ok, %s, I'm thinking of a number between 1 and 100. Try to guess what it is." %name)
    print("You have %s guesses to get it." %MAX)

    secretNum= getSecretNum()
    guessTime= 1
    while guessTime<=MAX:
        guessNum= ""
        while not checkInput(guessNum):
            guessNum= input("> Guess %s: " %guessTime)
        
        result= checkGuess(int(guessNum), secretNum)
        print(result)
        
        if guessNum==secretNum:
            print("You got my number [%s] in %s!" % (secretNum, guessTime))
            break
        if guessTime==MAX:
            print("You ran out of guesses! The number was [%s]" %secretNum)
        guessTime+= 1
        
    if not playAgain():
        break
