#eExample 8: Define a function 'lcm' that calculates the least common multiple (LCM) of two numbers, 'x' and 'y'.

x=input("Enter a number: ")
y=input("Enter a number: ") 
if x > y:
        z = x
else:
        z = y
    
# Use a 'while' loop to find the LCM.
while True:
        # Check if 'z' is divisible by both 'x' and 'y' with no remainder.
   if (z % x == 0) and (z % y == 0):
            # If both conditions are met, 'z' is the LCM, so store it in 'lcm' and break the loop.
            lcm = z
            break
        # If the conditions are not met, increment 'z' and continue checking.
            z += 1
    
    # Return the calculated LCM.
    #
print("LCM is:",lcm)


