import numpy as np

# reorgainzing arrays
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
before.shape

# changing the shape of the array - should be compatible
after = before.reshape(4, 2)
after

# vertically stacking matrices
vert_1 = np.array([1, 2, 3, 4])
vert_2 = np.array([5, 6, 7, 8])

print(np.vstack([vert_1, vert_2, np.ones((4), dtype="int32")]))

# horizontally stacking arrays
print(np.hstack([vert_1, vert_2]))