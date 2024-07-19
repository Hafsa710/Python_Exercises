#Example 5: Building CAR Game

A=""
while A.lower() !="quit":
    A= input("Enter Command: ").lower()
    if A=="start":
     print("Car started...")
    elif A=="stop":
      print("Car stopped...")
    elif A=="help":
       print("""
       Start- to start the car.\n
       Stop  - to stop the car.\n
       Quit-  to quit""")
    elif A=="quit":
     print("program Ended")
     break
    else:
     print("i can't understand")


# >>Output/Runtime Test Cases:
#  Enter Command: help

#        Start- to start the car.

#        Stop  - to stop the car.

#        Quit-  to quit
# Enter Command: stop
# Car stopped...
# Enter Command: quit
# program Ended