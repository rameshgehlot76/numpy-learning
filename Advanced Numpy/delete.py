"""
Delete Elements from a NumPy Array
np.delete(array, index, axis=None)
flatten the array if axis is None, otherwise delete along the specified axis.


"""

import numpy as np

arr_1d = np.array([10, 20, 30, 40, 50, 60])
print(arr_1d)

new_arr = np.delete(arr_1d, 0)
print(new_arr)



arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

new_arr_2d = np.delete(arr_2d, 1, axis=0)
print(new_arr_2d)


