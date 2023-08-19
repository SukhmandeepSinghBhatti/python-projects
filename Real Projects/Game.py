import random
name = input("Enter your name: ")
randNumber = random.randint(1,101)
UserGuess = None
Guess = 0

while (UserGuess != randNumber):
     UserGuess = int(input("Enter the guess: "))
Guess += 1
if (randNumber == UserGuess):
      print("You guess right!")
else:
     if (UserGuess > randNumber):
       print("You guess wrong! Enter a smaller number") 
     else:
      print("You guess wrong! Enter a larger number")  
print(f"You guess the number in {Guess} Guesses ")
Result = f"The name of the player is {name} and its score is {Guess}. "
with open("Game data.txt","a") as f:
    a = f.write(str(Result))
    f.write("\n")
 