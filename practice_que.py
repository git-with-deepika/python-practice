# list basic question
# even element of list
'''li=[1,2,3,4,5,6,7,8,9,10]
for element in li:
    if element%2==0:
        print(element,end=' ')
#sum and avg of avg
li=[1,2,3,4,5]
sum=0
count=0
for i in li:
    count+=1
    sum+=i
print(sum)
print(count)    
avg=sum/count
print(avg)

# largest element in list
li=[1,4,2,3,5]
larg=0
for i in range(1,len(li)):
    if larg<li[i]:
        larg=li[i]
print(larg)        
        
li=[4,2,3,5,1]
small=li[0]
for i in range(1,len(li)):
    if small>li[i]:
        small=li[i]
print(small)   

#Count how many times a given element appears in a list.
li=[1,2,2,3,4,2]
n=int(input("enter"))
count=0
for i in range(len(li)):
   if n==li[i]:
      count+=1
print(count)    

#Reverse a list using a for loop.
li=[1,4,2,3,5]
rev=[]
for i in range(len(li)-1,-1,-1):
    rev.append(li[i])
print(rev)    

#Remove duplicate elements from a list.
li=[1,2,3,2,3,4,6,5,7]
unique=[]
for i in li:
    if i not in unique:
        unique.append(i)

#Merge two lists into a single list.
li=[1,2,3,4]
li1=[5,6,7,8]
for i in range(len(li1)):
    li.append(li1[i])
print(li)    

# Sort a list in ascending order without using sort().
        


# Intermediate
#Move all zeroes to the end of a list.
li=[1,0,2,3,7,0,4]
remove=[]
for i in li:
    if i != 0:
        remove.append(i)
print(remove)

# Find the second largest element in a list.
li=[1,4,2,3,5,7,6]
first_larg=0
second_large=0
for i in li:
    if i > first_larg:
        second_larg=first_larg
        first_larg=i
    elif i >second_larg:
        second_larg=i
print(f'first_larg:{first_larg}')   
print(f'second_larg:{second_larg}') '''    
        
