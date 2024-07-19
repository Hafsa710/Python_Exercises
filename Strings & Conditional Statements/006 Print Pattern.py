#EXample 6:Set the value of 'n' to 5 (this will determine the number of lines in the pattern)
n = 5

# Iterate through the range of numbers from 0 to 'n' 
for i in range(n):
    
    for j in range(i):

        print('* ', end="")
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('') 
	