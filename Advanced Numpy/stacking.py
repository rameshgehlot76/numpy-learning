"""
vertically stack the arrays
horizontally stack the arrays

vstack() row wise
hstack() column wise

"""

import numpy as np

arr_1 = np.array([[1, 2, 3]])
arr_2 = np.array([[4, 5, 6]])

print(np.vstack((arr_1, arr_2)))  #vertically stack
print(np.hstack((arr_1, arr_2)))  #horizontally stack


