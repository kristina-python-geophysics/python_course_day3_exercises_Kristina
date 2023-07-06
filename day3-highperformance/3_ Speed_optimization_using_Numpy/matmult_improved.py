# Program to multiply two matrices using nested loops
import numpy as np 

N = 250

# NxN matrix
X = np.random.randint(0, 100, (N, N))

# Nx(N+1) matrix
Y = np.random.randint(0, 100, (N, N+1))

# result is Nx(N+1)
result = np.zeros((N, N+1))

# matrix multiplication using numpy
result = np.dot(X,Y)

for r in result:
    print(r)
