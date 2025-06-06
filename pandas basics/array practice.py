import numpy as np
a = np.array([1,2,3,4,5])
print(a)
a[0] = 100
print(a)
print(a[0])
d = a[3:6]
print(d)
# basic operation in data science# #vector#
u = [1,9]
v = [6,1]
z = []
for n,m in zip (u,v):
 sum_of_vec = n+m
 z.append(sum_of_vec)
 print(sum_of_vec)
 #scalar multiplication# 
f = np.array([2,3,4,56,7,89])
g = np.array ([4,6,98,74,4,9])
scalar = 2 * f
print(scalar)
 #dot product#
dot_product = np.dot(f,g)
print(dot_product)
 # adding constant #
y = g + 1
print(y) 
# universal function#
mean_value = np.mean(g)
print(mean_value)
max_value = np.max(g)
print(max_value)
print(np.pi)
print([0,np.pi/2,np.pi])
t = [0,np.pi/2,np.pi]
b = np.sin(t)
print(b)
w = np.linspace(-2,2,9)
print(w)
q = np.linspace(0,2*np.pi,100)
k = np.sin(q)
print(q)
print(k)
import matplotlib.pyplot as plt
plt.plot(q,k)
plt.title('sine waves')
plt.xlabel("Angle [radians]")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()