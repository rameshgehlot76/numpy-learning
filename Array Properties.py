import numpy as np


#___________________________________________________________

#shape >> Returns the dimensions of the array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

print(arr_2d.shape)  
# Output: (2, 3)

#____________________________________________________________


#size >> Returns the total number of elements in array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_2d.size)  
# Output: 6


#____________________________________________________________


#ndim >> Returns the number of dimensions of the array

arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(arr_1d.ndim)  # Output: 1
print(arr_2d.ndim)  # Output: 2
print(arr_3d.ndim)  # Output: 3


#_____________________________________________________________


#dtype >> Returns the data type of the array elements
arr = np.array([1, 2, 3.4, 4.5])
print(arr.dtype)

# Output: float64

#______________________________________________________________


#itemsize >> Returns the size (in bytes) of each element in the array
arr = np.array([1, 2, 3], dtype=np.int32)
print(arr.itemsize)  

# Output: 4 (since int32 takes 4 bytes)

#______________________________________________________________


#astype() >> Returns a new array with the specified data type
arr = np.array([1.2, 2.5, 3.7])
print(arr.dtype)  # Output: float64  
arr_int = arr.astype(int)

print(arr_int)
print(arr_int.dtype)

# Output: [1 2 3]
#          int64


#______________________________________________________________


