#Example 9: Define a function called concatenate_list_data that takes a list as a parameter.
def concatenate_list_data(lst):
    result = ''  
    
    # Iterate through the elements in the list.
    for element in lst:
        result += str(element)  

    return result  # Return the concatenated string.

# Call the concatenate_list_data function with a list of numbers and print the result.
print(concatenate_list_data([1, 5, 12, 2]))
