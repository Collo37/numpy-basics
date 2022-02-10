import numpy as np

# initializing different types of arrays

# all zeros matrix
# use np.zeros(shape_of_the_matrix)
a = np.zeros((2, 3)) # output [[0 0 0], [0 0 0]]

# all ones matrix
np.ones((3, 3), dtype="int32") # output [[1 1 1], [1 1 1]]

# any other number
# takes in two arguments np.full(shape_of_the_matrix, value_of_the_elements)
np.full((2, 2), 99) # output [[99 99], [99 99]]

# full_like - replicates the shape of another array and fills it with the specified value
np.full_like(a, 99) # output [[99 99], [99 99]]

# initialzing a matrix of random decimal numbers
# np.random.rand(row, col) - do not pass the shape as a tuple
np.random.rand(3, 4)

# to pass a shape use random.random_sample
np.random.random_sample(a.shape)

# random integer values
np.random.randint(10, size=(3, 3))
np.random.randint(4, 10, size=(3, 3))

# identity matrix
# np.identity only takes one argument for the shape since its going to be a square
np.identity(3) # output [[1 0 0], [0 1 0], [0 0 1]]

# repeating an array
arr = np.array([2, 3, 4])
repeat = np.repeat(arr, 2)
repeat # output [2 2 3 3 4 4]

ones_array = np.ones((5, 5), dtype="int32")
zeros_array = np.zeros((3, 3), dtype="int32")

zeros_array[1, 1] = 9
ones_array[1:-1, 1: -1] = zeros_array

ones_array

# copying an array
a = np.array([1, 2, 3])
b = a.copy()

b[0] = 40

print(b)
print(a)