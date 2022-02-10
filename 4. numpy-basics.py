import numpy as np

# Mathematical functions of numpy
a = np.array([1, 2, 3, 4])

# accepts all mathematical operations in python
a + 2
a * 2
a / 2
a - 2

b = [1, 0, 1, 0]
# addition of two arrays
a + b

# sin functions
np.sin(a)
np.cos(a)

# LINEAR ALGEBRA

matrix_a = np.ones((2, 3), dtype="int32")
matrix_b = np.full((3, 2), 2)

# multiplying
np.matmul(matrix_a, matrix_b) # output [[6 6], [6 6]]

# getting the determinant of a matrix
identity_matrix = np.identity(3, dtype="int32") # an identity matrix has a determinant of one
np.linalg.det(identity_matrix) # output 1

# getting the inverse of a matrix
np.linalg.inv(identity_matrix)

# STATISTICS
stats = np.array([[1, 2, 3], [4, 5, 6]])

# minumum and maximum
np.min(stats)
np.max(stats)

# sum
np.sum(stats)