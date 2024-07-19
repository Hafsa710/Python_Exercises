#Example 6:Maximum & Minimum

def max_min(data):
    # Initialize two variables 'l' and 's' with the first element of the 'data' list.
    l = data[0]  
    s = data[0]  
    # Iterate through each number 'num' in the 'data' list.
    for num in data:
        
        if num > l:
            l = num  
        
        elif num < s:
            s = num  #
    # Return the maximum 'l' and minimum 's' values as a tuple.
    return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))
