import numpy as np
#a. Create a null vector of size 10 but the fifth value which is 1
x=np.zeros(10)
x[4]=1
print(x)

#b. Create a vector with values ranging from 10 to 49
y=np.arange(10,50)
print(y)

#c. Reverse a vector (first element becomes last)
z = np.flip(y)
print(y)

#d. Create a 3x3 matrix with values ranging from 0 to 8
m = np.arange(0,9).reshape((3,3))
print(m)

#e. Find indices of non-zero elements from [1,2,0,0,4,0]
e = np.nonzero([1,2,0,0,4,0])
 print(e)

#f. Create a random vector of size 30 and find the mean value
r=np.random.random(30)
r_mean=np.mean(r)
print(r_mean)

#g. Create a 2d array with 1 on the border and 0 inside
 b=np.ones((5,5))
 print(b)
 b[1:-1,1:-1]=0
 print(b)
 
#h. Create a 8x8 matrix and fill it with a checkerboard pattern
 t=np.ones((3,3))
 t=np.zeros((8,8), dtype=int)
 t[1::2,::2]=1
 t[::2,1::2]=1
