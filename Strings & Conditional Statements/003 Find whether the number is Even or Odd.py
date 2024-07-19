#Example 3: WAP to check if a number entered by the user is odd or even

num= int(input("Enter the number:"))
rem= num % 2

if(rem==0):
    print("Even")

else:
  print("Odd")

# >>Output/Runtime Test Cases:
# Enter the number:5
# Odd  
# Enter the number:68
# Even