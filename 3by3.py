
import math

# Define the system of equations
# 2x + y + z = 10
# x - y + 3z = 0
# 3x + 4y - 2z = 2

a11 = float(input("a11: "))
a12 = float(input("a12: "))
a13 = float(input("a13: "))
b1 = float(input("b1: "))

a21 = float(input("a21: "))
a22 = float(input("a22: "))
a23 = float(input("a23: "))
b2 = float(input("b2: "))

a31 = float(input("a31: "))
a32 = float(input("a32: "))
a33 = float(input("a33: "))
b3 = float(input("b3: "))

# Define the augmented matrix
matrix = [[a11, a12, a13, b1],
          [a21, a22, a23, b2],
          [a31, a32, a33, b3]]

# Perform Gaussian elimination to obtain an upper triangular matrix
for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):
        factor = matrix[j][i] / matrix[i][i]
        for k in range(i, len(matrix[0])):
            matrix[j][k] -= factor * matrix[i][k]

# Back-substitution to obtain the solutions
z = matrix[2][3] / matrix[2][2]
y = (matrix[1][3] - matrix[1][2]*z) / matrix[1][1]
x = (matrix[0][3] - matrix[0][1]*y - matrix[0][2]*z) / matrix[0][0]

# Print the solutions
print("x =", x)
print("y =", y)
print("z =", z)
