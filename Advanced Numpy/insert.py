"""
np.insert(array, index, values, axis=None)
array - original array
index - index before which values is inserted
value - values to be inserted into array
axis - axis along which to insert values. If axis is None, array is flattened first.
axis = 0 - insert along rows
axis = 1 - insert along columns

"""

import numpy as np

arr_1d = np.array([10, 20, 30, 40, 50, 60])
print("Original 1D array:")
print(arr_1d)


print("\nInserting 25 at index 2:")

new_arr_1d = np.insert(arr_1d, 2, 25)
print(new_arr_1d)

