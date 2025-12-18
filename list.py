# list is sequence data type which store data or value in a sequence
'''new_list=[1,2,3]
details=['ram','A23',12673]
print(type(details))
print(new_list)
print(details)

# accessing elements of list
# since list is a sequence data type we can access element of list by index
print(f'Name : {details[0]}')
print(f'batch : {details[1]}')
print(f'mob :  {details[2]}')

# slicing: into this we retive a sublist of the list [start : end : step]
print(details[0:2])
# list is mutable : it could be change after the creation of list

li=[1,2,3,4]
print(f'old list: {li}')
li[0]=10
print(f'new list: {li}')

# list using for loop :- using index
li=[10,20,30,40]
for index in range(4):
    print(li[index],end=" ")
# index of the element
li=[10,20,30,40]
for index in range(4):
    print(index,end=" ")

# using len() function
li=[10,20,30,40]
for index in range(len(li)):
    print(li[index],end=" ")

# accessing element without index
li=[10,20,30,40]
for element in li:
    print(element,end=" ")

# sum of list element
li=[10,20,30,40]
sum=0
for element in li:
    sum+=element
print(sum)

# product of list element
li=[1,2,3,4,5,6]
prod=1
for element in li:
    prod*=element
print(prod)

# even element
li=[1,2,3,4,5,6]
for element in li:
    if element%2==0:
        print(element)
# even index element   
li=[1,2,3,4,5,6]
for index in range(len(li)):
    if index%2==0:
        print(li[index])
# squre of list element
li=[1,2,3,4]
for i in range(len(li)):
    li[i]=li[i]*2
print(li)   

#add 2 in each element
li=[1,2,3,4]
for i in range(len(li)):
    li[i]=li[i]+2
print(li)'''

# addtion  of two list
li=[1,2,3,4]
li1=[5,6,7,8]
for i in range(len(li)):
    li[i]=li[i]+li1[i]
print(li)    
    