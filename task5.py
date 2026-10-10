import numpy as np

print("TASK 5: Matrix Operations")

A = np.array([[2, 1, 3],
              [0, 4, 2],
              [1, 5, 2]])
B = np.array([[1, 3, 0],
              [2, 1, 4],
              [3, 0, 2]])

print("Shape of A:", A.shape)
print("Shape of B:", B.shape)

print("Shapes for addition:", A.shape, B.shape)
print("A + B:\n", A + B)
print("Shapes for subtraction:", A.shape, B.shape)
print("A - B:\n", A - B)
print("Shapes for element-wise multiplication:", A.shape, B.shape)
print("A * B:\n", A * B)
print("Shapes for matrix multiplication:", A.shape, B.shape)
print("A @ B:\n", A @ B)

print("Shape of A before transpose:", A.shape)
print("Shape of A transpose:", A.T.shape)
print("A transpose:\n", A.T)

print("Shape of A for determinant:", A.shape)
determinant = np.linalg.det(A)
print("Determinant of A:", determinant)

if determinant != 0:
    print("Shape of A for inverse:", A.shape)
    inverse_A = np.linalg.inv(A)
    print("Inverse of A:\n", inverse_A)
else:
    print("A has determinant zero, so its inverse does not exist.")

print("Addition, subtraction and element-wise multiplication need equal or")
print("broadcast-compatible shapes. For A @ B, the number of columns in A")
print("must equal the number of rows in B. Determinants and inverses need")
print("square matrices; an inverse exists only if the determinant is non-zero.")
