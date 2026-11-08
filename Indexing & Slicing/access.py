"""
array[index]        #1d array indexing
array[row, column]  #2d array indexing
"""

import numpy as np

arr = np.array([11,22,33,44,55])

print(arr[0])  # Output: 11
print(arr[2])  # Output: 33
print(arr[-1]) # Output: 55


array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])

print(array_2d[0, 1])  # Output: 2
print(array_2d[1, 2])  # Output: 6
print(array_2d[0, -1]) # Output: 3
print(array_2d[-1, -1]) # Output: 6


