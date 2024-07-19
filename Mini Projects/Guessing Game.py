
# #Guessing Game

import random

target=random.randint(1,100)

while True:
  userChoice=(input("Guess the target or QUIT:"))
  if(userChoice== "QUIT"):
      break
  if (userChoice==target):
    print("You have successfully guessed the number")
    break
  elif(userChoice < target):
    print("your number was too small.Take bigger guess..")

  else:
    print("Your number was too big.Take a smalller guess..")


print("-----Game Over")