
# Online Python - IDE, Editor, Compiler, Interpreter
import numpy as np

# Create a random vector of size 15 with integers in the range 1-20
random_vector = np.random.randint(1, 21, size=15)

# Reshape the vector to a 3x5 array
reshaped_array = random_vector.reshape(3, 5)

# Replace the maximum value in each row with 0
max_replaced_array = reshaped_array.copy()
for i in range(max_replaced_array.shape[0]):
    max_replaced_array[i, max_replaced_array[i].argmax()] = 0

print("Original array:\n", reshaped_array)
print("Array after replacing max in each row with 0:\n", max_replaced_array)




