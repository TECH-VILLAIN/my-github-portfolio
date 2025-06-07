import numpy as np
a = np.array([[1,3,4],
             [4,5,6]])
print (a)
b = 2 * a
print(b)
c = np.array([[3,4,],
               [9,6],
               [4,5]])
g = np.dot(a,c)
print(g)
 # excercise#
A = np.array([[2, 4],
     [6, 8]])

B = np.array([[1, 3],
     [5, 7]])
#Scalar multiplication of A by 3#
v = A * 3
print(v)
#Element-wise multiplication of A and B#
r = A * B
print(r)
#Matrix multiplication of A and B#
y = A @ B 
print(y)
#or#
u = np.dot(A,B)
print(u)
#transpose#
i = A.T
print(i)