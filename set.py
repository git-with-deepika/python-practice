# set is a data type in python used to store unique values
# set is unorded collection of elements
# initialization of set : the set can be initializite with curly braces {}  but there should some elements into that
s1={1,2,3}
print(type(s1))

# if you want to create a empty set then you have to use set() constructor
s2=set()
#print(type(s2))
# set is unordered collection of elements and it is mutable and store unique elements
# the set stores the unique elements
s={1,2,3,3,4,5,6,6}
print(s)

# creating set from list
li=[1,2,3,4]
new=set(li)
print(new)

#  set is an unordered collection of elements so we can't access elements usind index insted we use membership operator (in operator)
s={1,2,3,4,5,6}
for element in s:
  print(element,end=' ')


# adding element in set
print()
s={1,2,3,4,5,6}
s.add(7)
print(s)

# update method is used to update or add multiple elements into existing set
s.update([1,2,4,9,10,'new_st','hello'])
print(s)

# wap to creat a set using list of elements
li1=[1,2,3,4,5,5,6,7]
new_set=set(li1)
print("new_set: ",new_set)

#write a program that take 5 input from user and add each into set
st=list(map(int,input("enter number").split()))
print(st)
new=set(st)
print("set is : ",new)

###########
st=set(list(map(int,input("enter number").split())))
print(st)
#another way way to take 5 input from user
number=[]
for i in range(5):
  n=int(input("enter number: "))
  number.append(n)
print(number)

new_no=set(number)
print("new_set is: ",new_no)


# using while loop  
s=set()
n=5
while n>0:
  element=int(input("enter number: "))
  s.add(element)
  n-=1

# discard is used   to remove the particular element from the set  if the element present into the set it will remove that element otherwise it will not through an error
s={1,2,3,4,5,6}
s.discard(6)
print(s)
# remove shows an error if element nor present

# pop method is used to random element from set and return it
s={1,2,3,4,5,6}
s.pop()

se={1,2,3,4,5}
se1={4,5,6,7,8}



