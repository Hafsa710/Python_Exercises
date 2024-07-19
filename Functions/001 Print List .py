#Print List Using Method

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits=["mango","grapes","apple","litchi"]
print_list(fruits)

# >>Output/Runtime Test Cases:
# mango
# grapes
# apple 
# litchi