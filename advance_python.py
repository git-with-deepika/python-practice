# Introduction to numpy :- 
# numpy = num(numerical) + py(python)
# this is an open source library of python and this is used for scientific calculation
# list is hetrogenous data type and numpy is homogenous data type

a= [1,2,3]
print(a*3)

import numpy as np
b=np.array([1,2,3])
print(b*3)

new=[1,2,3]
new_a=np.array(new)
print(new_a)
print(type(new))
print(type(new_a))


li=[[1,2,3],[4,5,6],[7,8,9]]
li1=np.array(li)
print(li1)

# Row=3 r_1=[1,2,3],r_2=[4,5,6],r_3=[7,8,9]
# colum=3 c_1=[1,4,7],c_2=[2,5,8],c_3=[3,6,9]

print("total shape: ",li1.shape) # shape= row,column
print("total elements: ", li1.size) # size=row*column
print("total dimension: ",li1.ndim)  # total dimension=2


# pre-built function of numpy

# 1. zeros() :-  it will create an array in which all the values will be 0 in euther one dimension 
#                or multi-dimension

Li=np.zeros(3)
print(Li)

Li2=np.zeros((3,4))
print(Li2)

# 2. ones():- it will create an array in which all the values will be 1 in euther one dimension 
#                or multi-dimension
Li3=np.ones(3)
print(Li3)

Li4=np.ones((3,4))
print(Li4)

# 3. eye(): it will create an array in which digonal position elements are 1 and rest all 0
c=np.eye(4)
print(c)

# 4. diag() :- it will set custom values on diagonal position
d=np.array((23,45,67,89))
print(d)
new_d=np.diag(d)
print(new_d)

# 5 Random module:
# (a)randint():- it will create random number in a given range
# syntax:- np.random.randint(min_range,max_rane,total_numbers)

ran=np.random.randint(1,10,3)
print(ran)

# (b) rand():- it will create random numbers in range 0-1
rand_num=np.random.rand(5)
print(rand_num)

# (c) seed():- it will fix our random generated numbers
np.random.seed(3)
new_num=np.random.randint(1,10,4)
print(new_num)
