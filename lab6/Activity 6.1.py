import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

def mat_desc(matrix):

    if matrix.size > 0:
        is_square = True if matrix.shape[0] == matrix.shape[1] else False
        print(f'Matrix:\n{matrix}\n'
          f'\nShape:\t{matrix.shape}'
          f'\nSize: \t{matrix.size}'
          f'\nRank:\t{matrix.ndim}'
          f'\nSquare: {is_square}'

          )

        Sum = sum(matrix)
        sums = sum(Sum)
        diagonal = np.diagonal(matrix)
        result = 1
        for x in diagonal:
            result = result * x

        if sums == 0:
            print("Zero:", True)
            print("Ones:", False)
            print('Identity:', False)

        elif sums == matrix.size:
            print("Zero:", False)
            print("Ones:", True)
            print('Identity:', False)

        elif result == 1:
            print("Zero:", False)
            print("Ones:", False)
            print('Identity:',True)
        else:
            print("Zero:", False)
            print("Ones:", False)
            print('Identity:', False)

    else:
        print('Matrix is Null')


A = np.zeros([4, 4])
B = np.ones([5, 5])
C = np.identity(5)
D = np.array([[7, 7], [6, 4]])
E = np.array([[8, 8], [7, 4]])
mat_desc(A)
print("#" * 64)
mat_desc(B)
print("#" * 64)
mat_desc(C)
print("#" * 64)
mat_desc(D)
print("#" * 64)
mat_desc(E)
print("#" * 64)