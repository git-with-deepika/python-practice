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


# 6. view vs copy :- view means changes in the original data and copy means changes in duplicate 
#                    data will not reflact the original data

arr=np.array([10,20,30,40,50,60,70,80])
print(arr)
arr[3:6]=0
print(arr)


cp=np.array([10,20,30,40,50,60,70,80])
new_cp=cp[3:6].copy()
new_cp[:]=0
print(new_cp)


# opetaions in array
# (1) arange() :- it works as for loop in numpy
a=np.arange(1,16,1)
print(a)


a > 10
print(a)


b = a > 10
print(a[b])

b= a%2==0
print(a[b])

# (2) reshaping():-
# reshaping condition
# n(rows) * n(colunm)=n(total_elements)
a=np.random.randint(1,50,12)
print(a)

a.reshape(2,6)
print(a)

a.reshape(3,4)
print(a)


a=np.arange(1,5).reshape(2,2)
print(a)

b=np.arange(5,9).reshape(2,2)
print(b)

print(a+b)
print(a-b)
# not matrix multiplication
print(a*b)

# matrix multiplication
print(a.dot(b))


a=np.arange(1,5)
print(a)
print(a**2)
print(a**3)

print(np.sqrt(a))
print(np.sin(a))
print(np.cos(a))

# (3) linspace() :- it will return same gape values in given range
a=np.linspace(1,2,5)
print(a)

# (4) unique() :- it will rwturn 3 array
# arr  -> return original values of array
# return_index -> True-> return index value of unique numbers 
# return_counts -> True -> it will return total fequency of each unique values

a=np.array([1,2,2,3,2,2,3,4,5,5,6])
print(a)

a=np.unique(a,return_index= True, return_counts=True)
print(a)


# hstack() and vstack()
# hstack():- it will add 2 or more array horizontally
# vstack():-it will add 2 or more array vartically

a=np.arange(1,5).reshape(2,2)
b=np.arange(5,9).reshape(2,2)
c=np.arange(9,13).reshape(2,2)
print(np.hstack((a,b,c)))
print(np.vstack((a,b,c)))