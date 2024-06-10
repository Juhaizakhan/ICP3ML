
# Online Python - IDE, Editor, Compiler, Interpreter
import numpy as np

square_array = np.array([[4, -2], [1, 1]])
eigenvalues, eigenvectors = np.linalg.eig(square_array)

print("Eigenvalues:", eigenvalues)
print("Right eigenvectors:\n", eigenvectors)




