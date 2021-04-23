import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

def mat_operations(matrix1, matrix2):
    if np.isscalar(matrix1) == True and np.isscalar(matrix2) == True:
        print(matrix1, 'Is a scalar')
        print(matrix2, 'Is a scalar')
        print('#' * 64)
################################################################################
    elif np.isscalar(matrix1) == True:
        print(matrix1,'Is a scalar')
        print('#'*64)
        if matrix2.size > 0:
            is_square = True if matrix2.shape[0] == matrix2.shape[1] else False
            print(f'Matrix:\n{matrix2}\n'
                  f'\nShape:\t{matrix2.shape}'
                  f'\nSize: \t{matrix2.size}'
                  f'\nRank:\t{matrix2.ndim}'
                  f'\nSquare: {is_square}\n',
                  f'=' * 64)
        else:
            print('Matrix is Null')
################################################################################
    elif np.isscalar(matrix2)==True:
        print(matrix2,'Is a scalar')
        print('#' * 64)
        if matrix1.size > 0:
            is_square = True if matrix1.shape[0] == matrix1.shape[1] else False
            print(f'Matrix:\n{matrix1}\n'
                  f'\nShape:\t{matrix1.shape}'
                  f'\nSize: \t{matrix1.size}'
                  f'\nRank:\t{matrix1.ndim}'
                  f'\nSquare: {is_square}\n',
                  f'=' * 64)
        else:
            print('Matrix is Null')
################################################################################
    elif np.isscalar(matrix1) == False and np.isscalar(matrix2) == False:
        if matrix1.size > 0 and matrix2.size > 0:
            is_square = True if matrix1.shape[0] == matrix1.shape[1] else False
            print(f'Matrix:\n{matrix1}\n'
                  f'\nShape:\t{matrix1.shape}'
                  f'\nSize: \t{matrix1.size}'
                  f'\nRank:\t{matrix1.ndim}'
                  f'\nSquare: {is_square}\n',
                  f'=' * 64)
            is_square = True if matrix2.shape[0] == matrix2.shape[1] else False
            print(f'Matrix:\n{matrix2}\n'
                  f'\nShape:\t{matrix2.shape}'
                  f'\nSize: \t{matrix2.size}'
                  f'\nRank:\t{matrix2.ndim}'
                  f'\nSquare: {is_square}\n',
                  f'=' * 64)
        else:
            print('Matrix is Null')
################################################################################
    if np.isscalar(matrix1)==True:
        addition = matrix1 + matrix2
        substraction = matrix1 - matrix2
        multiplication = matrix1 * matrix2
        division = matrix1 // matrix2
        print(addition)
        print(substraction)
        print(multiplication)
        print(division)
################################################################################
    elif np.isscalar(matrix2) == True:
        addition = matrix1 + matrix2
        substraction = matrix1 - matrix2
        multiplication = matrix1 * matrix2
        division = matrix1 // matrix2
        print(addition)
        print(substraction)
        print(multiplication)
        print(division)
################################################################################
    elif matrix1.size == matrix2.size :
        addition = matrix1 + matrix2
        substraction = matrix1 - matrix2
        multiplication = matrix1 * matrix2
        division = matrix1 // matrix2
        print(addition)
        print(substraction)
        print(multiplication)
        print(division)
################################################################################
    else:
            print("Cannot perfrom operations due to unequal matrix size")
################################################################################
A = np.array([[4, 4], [3, 4]])
B = np.array([[5, 5], [4, 4]])
C = -3
D = np.array([[7, 7], [6, 4],[7,9]])
E = 5
################################################################################
mat_operations(A, B)
print("#" * 64)
mat_operations(A,C)
print("#" * 64)
mat_operations(A,D)
print("#" * 64)
mat_operations(C,E)
print("#" * 64)
