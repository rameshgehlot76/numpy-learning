#np.nan_to_num(array, nan=value) default = 0
import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])

# gives default value 0 
cleaned_arr = np.nan_to_num(arr)
print(cleaned_arr)

# gives given value 
cleaned_arr_1 = np.nan_to_num(arr, nan=99)
print(cleaned_arr_1)


