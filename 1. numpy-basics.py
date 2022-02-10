import numpy as np

# initializing an array
a = np.array([1, 2, 3, 4])

# 2D array
b = np.array([[9.0, 8.0, 6.0], [2.4, 5.5, 0.5]])

# getting the dimensions of an array
a.ndim # output 1
b.ndim # output 2

# getting the shape of an array
# this outputs a tuple of the dimensions of the shape of the array

a.shape # output 4 (one dimension arrays returns the length of the array)
b.shape # output (2, 3)

# getting the data type
a.dtype # output int32
b.dtype # output float32

# we can also set the data type when initializing an array
a2 = np.array([2, 4, 6, 8], dtype="int16")
a2.dtype # output int16

# getting the item size
a.itemsize # output 8
b.itemsize # output 8
a2.itemsize # output 2

# getting the total size
a.size * a.itemsize # similar to a.nbytes output = 32
b.size * a.itemsize # similar to b.nbytes output = 48

