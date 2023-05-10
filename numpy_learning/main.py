import numpy as np

# Create an array of ones
ones_array = np.ones((3, 4))
print("Ones Array:")
print(ones_array)
print()

# Create an array of zeros
zeros_array = np.zeros((2, 3, 4), dtype=np.int16)
print("Zeros Array:")
print(zeros_array)
print()

# Create an array with random values
random_array = np.random.random((2, 2))
print("Random Array:")
print(random_array)
print()

# Create an empty array
empty_array = np.empty((3, 2))
print("Empty Array:")
print(empty_array)
print()

# Create a full array
full_array = np.full((2, 2), 7)
print("Full Array:")
print(full_array)
print()

# Create an array of evenly-spaced values
arange_array = np.arange(10, 25, 5)
print("Arange Array:")
print(arange_array)
print()

# Create an array of evenly-spaced values
np.linspace(0,2,9)