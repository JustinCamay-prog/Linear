import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la


A = np.array([[4, 4], [3, 4]])
B = np.array([[5, 5], [5, 4]])
C = np.array([[6, 6], [6, 4]])
D = np.identity(2)
E = np.zeros(2)

def Commutative_Property(Matrix1,Matrix2):
    CP_AnswerAB = np.dot(Matrix1, Matrix2)
    CP_AnswerBA = np.dot(Matrix2, Matrix1)
    print(CP_AnswerAB,'\n    ≠   \n',CP_AnswerBA,)
    print( '#'*64)

def Associative_Property(Matrix1, Matrix2, Matrix3):

    AP_AnswerBC = np.dot(Matrix2, Matrix3)
    AP_AnswerBCA = np.dot(Matrix1, AP_AnswerBC)
    AP_AnswerAB = np.dot(Matrix1, Matrix2)
    AP_AnswerABC = np.dot(AP_AnswerAB, Matrix3)
    print(AP_AnswerABC,'\n    =\n',AP_AnswerBCA)
    print('#'*64)

def Distributive_Property(Matrix1, Matrix2, Matrix3):
    DP_AnswerBC = np.add(Matrix2, Matrix3)
    DP_AnswerABC = np.dot(Matrix1, DP_AnswerBC)
    DP_AnswerAB = np.dot(Matrix1, Matrix2)
    DP_AnswerAC = np.dot(Matrix1, Matrix3)
    print(DP_AnswerABC,'\n   =\n', DP_AnswerAB+ DP_AnswerAC)
    print('#'*64)
    DP_AnswerBCA = np.dot(DP_AnswerBC,Matrix1)
    DP_AnswerBA =np.dot(Matrix2, Matrix1)
    DP_AnswerCA =np.dot(Matrix3, Matrix1)
    print(DP_AnswerBCA,'\n    =\n',DP_AnswerBA + DP_AnswerCA)
    print('#'*64)

def Multiplicative_Identity_Property(Matrix1, I):
    MIP_Answer = np.dot(Matrix1,I)
    print(MIP_Answer,'\n   =\n',Matrix1)
    print('#'*64)

def Multiplicative_Property_of_zero(Matrix1,Zero):
    MPZ_Answer = np.dot(Matrix1,Zero)
    print(MPZ_Answer,'\n   =\n',Zero)

Commutative_Property(A,B)
Associative_Property(A,B,C)
Distributive_Property(A,B,C)
Multiplicative_Identity_Property(A,D)
Multiplicative_Property_of_zero(A,E)