
# Online Python - IDE, Editor, Compiler, Interpreter
import numpy as np

random_vector = np.random.randint(1, 21, size=15)
reshaped_array = random_vector.reshape(3, 5)

for i in range(reshaped_array.shape[0]):
    reshaped_array[i, np.argmax(reshaped_array[i])] = 0

print("Original reshaped array:\n", reshaped_array)





