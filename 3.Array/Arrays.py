import array

my_array = array.array('i')
print(my_array)
my_array1 = array.array('i',[1,2,3,4,5,6,7,8])
print(my_array1)

# insert in array
my_array1.insert(8,11)
print(my_array1)


import numpy as np

np_array = np.array([],dtype = int)
print(np_array )
np_array1 = np.array([1,2,3,4])
print(np_array1)