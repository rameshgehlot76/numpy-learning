"""
array[start:stop:step] # Slicing syntax in NumPy
array[start:stop]      # Slicing with default step of 1
                       # start to end -1 

"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[1:5])   # Output: [20 30 40 50]
print(arr[:4])    # Output: [10 20 30 40]
print(arr[2:])    # Output: [30 40 50 60]
print(arr[::2])   # Output: [10 30 50]
print(arr[1:5:2]) # Output: [20 40]
print(arr[::-1])  # Output: [60 50 40 30 20 10]


array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

print(array_2d[0:2, 1:3])  # Output: [[2 3]
print(array_2d[1:, :2])    # Output: [[4 5]
print(array_2d[:, 1:])     # Output: [[2 3]
