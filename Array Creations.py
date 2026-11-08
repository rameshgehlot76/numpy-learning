#creating array from python lists
#np.array([ele1, ele2, ele3, ...])

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# [1 2 3 4 5]



#with default values 
#np.zeros(shape) (3) for 1D, (3,3) for 2D,

import numpy as np 
zeros_array = np.zeros(5)
print(zeros_array)

# [0. 0. 0. 0. 0.]



#ones(shape) 
ones_array = np.ones((2,3)) 
print(ones_array)

# [[1. 1. 1.]
#  [1. 1. 1.]]



#full(shape, fill_value)
full_array = np.full((2,3), 7)
print(full_array)

# [[7 7 7]
#  [7 7 7]]



#creating sequence of numbers in numpy
#arange()
#arange(start, stop, step) 
arange_array = np.arange(0, 10, 2)
print(arange_array)

# [0 2 4 6 8] 



#creating identity matrices
#eye(size)
identity_matrix = np.eye(4)
print(identity_matrix)

'''
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
 
'''
 
 
