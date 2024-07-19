#Example 2:Search for a number in List
nums=[1,4,9,16,25,36,49,64,81,100]
x=81
i=0
while i< len(nums):
    if (nums [i]==x):
        print("Number:",x)
        print("Found at index",i)
    i+=1

# >>Output/Runtime Test Cases:
# Number: 81
# Found at index 8