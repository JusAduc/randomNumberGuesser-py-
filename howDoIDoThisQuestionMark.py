import random as r 
ranNum= r.randint(1,100)
NumbersAiGuessed=[]
def aiGuess():
    ranGuess=r.randint(1,100)
    if ranGuess in NumbersAiGuessed:
        ranGuess=r.randint(1,100)
    else:
        NumbersAiGuessed.append(ranGuess)
    if ranGuess==ranNum:
        print("Done")
        print("The random Number was: ")
        print(ranGuess)
        print("This is the array: ")
        print(NumbersAiGuessed)
        print("Ammount of Guesses: ",len(NumbersAiGuessed))
    else:
        aiGuess()
aiGuess()