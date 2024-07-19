#Example 4:WAP to find the greatest of 3 numbers entered by the user.

a=int(input("Enter a First number:"))
b=int(input("Enter a Second number:"))
c=int(input("Enter a Third number:"))
if(a>=b and a>=c):

    print("A is greatest")

elif(b>=a and b>c):

    print("B is greatest")

elif(c>=b and c>=a):

    print("C is greatest")


#>>Output/Runtime Test Cases:
# Enter a First number:45
# Enter a Second number:78
# Enter a Third number:23
# B is greatest