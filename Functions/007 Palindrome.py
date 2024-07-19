import numpy as np
a = np.array([[10, 4], [8, 12]])
b = np.array([[15, 6]])
c = np.concatenate((a, b), axis=0)
def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    # s = s.replace(" ", "").lower()
    return s == s[::-1]