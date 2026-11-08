"""
.ravel()  -> view of the array, flattened to one dimension
.flatten() -> copy of the array, flattened to one dimension

"""

import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2D array:")
print(arr_2d)

print("\nUsing .ravel()")
print(arr_2d.ravel())

print("\nUsing .flatten()")
print(arr_2d.flatten())

