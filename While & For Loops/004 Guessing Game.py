# Example 4:Guessing Game
Secert_number=4
i=0
j=3
while i<j:
    H = int(input ("Guess the Number:"))
    i+=1
    if H == Secert_number:
        print("you won!!")
        break
else:
    print("No of Attempts Ended")