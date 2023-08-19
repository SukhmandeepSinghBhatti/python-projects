import random
from wsgiref.util import guess_scheme
randNumber = random.randint(1,100)
print(randNumber)
userGuess = None
Guess = 0
while (userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    Guess += 1
    if (userGuess==randNumber):
        print("You guess it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed wrong! Enter a larger number ")
print(f"You guess the number in {Guess} guesses")

       # Under development --> 

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(userGuess<hiscore):
    print("You have just broken the high score!")
with open("hiscore.txt", "a") as f:
        f.write((userGuess))
        