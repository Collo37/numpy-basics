import numpy as np

# Accessing/changing specific elements, rows, columns, etc
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# getting a specific element
# use the [row, column] syntax
a[1, 5] # output 13

# getting a specific row
a[1] # output [8, 9 , 10, 11, 12, 13, 14]

# getting a specific column
a[:, 4] # output [5 12] (fifth column of both arrays)

# further indexing [startindex: endindex: stepsize]
a[0, 1: 6: 2] # output [2 4 6] starts at the second first array, second element to the seventh element and skips two

# changing a value
# changing the last element in the first array
(a[0,-1]) = 20
(a[0]) # output [1 2 3 4 5 6 20]

# 3D example
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# getting a specific element
b[0, 1, -1] # output 4

# replacing a value in the 3D array
b[:, 1] = [[9, 10], [11, 12]]
print(b) # output [[[1 2], [9 10]], [[5 6], [11 12]]]