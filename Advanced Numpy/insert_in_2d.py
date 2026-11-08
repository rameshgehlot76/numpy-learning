import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)

# insert a new row at index 1
new_arr_2d = np.insert(arr_2d, 1, [11, 12, 13], axis=0)
print("\nInserting a new row at index 1:")
print(new_arr_2d)


# insert a new column at index 2
new_arr_2d_col = np.insert(arr_2d, 2, [14, 15, 16], axis=1)
print("\nInserting a new column at index 2:")
print(new_arr_2d_col)


# insert in a single line flattened array
#new_arr_flat = np.insert(arr_2d, 4, [17, 18, 19])
new_arr_flat = np.insert(arr_2d, 4, [17, 18, 19], axis=None)
print("\nInserting values in a flattened array at index 4:")
print(new_arr_flat)



