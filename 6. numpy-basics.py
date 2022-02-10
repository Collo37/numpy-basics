import numpy as np

# Loading data from a file
data = np.genfromtxt("data.txt", delimiter=",").astype("int32")

data

# Boolean masking and advanced indexing
data > 50 # returns an array of boolean values

# grabbing files greater than 50
data[data > 50] # output [[196  75 766  75  55 999  78  76  88]

np.any(data > 50, axis=0) # returns boolean value of any elements greater than 50 in the first vertical axis
np.all(data > 50, axis=0)# returns boolean value of all elements greater than 50 in the first vertical axis
print(data[(data > 40) & (data < 100)]) # returns values > 40 and less than 100
print(~data[(data > 40) & (data < 100)]) # returns inverse of values > 40 and less than 100


# indexing with an array
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a[[0, 4, -1]] # outputs [1, 5, 9]

