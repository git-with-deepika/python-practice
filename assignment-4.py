#square partten
n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end='')
    print()

#right-angled triangle partten
n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end='')
    print()   

# inverted right-angled triangle partten
n=int(input("enter n:"))
for i in range(n+1,1,-1):
    for j in range(i-1):
        print("*",end='')
    print()       

# triangle with numbers
n=int(input("enter n:"))
a=1
for i in range(n+1):
    for j in range(i):
        print((a+j),end='')
    print()

# same number triangle
n=int(input("enter n:"))

for i in range(1,n+1):
    for j in range(i):
        print(i,end='')
    print() 
# square number
n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end='')
    print() 
#Triangle of alphabets
n=int(input("enter n:"))
a=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(a+j),end='')
    print()



#Square of alphabets
n=int(input("enter n:"))
a=65
for i in range(n):
    for j in range(n):
        print(chr(a+i),end='')
    print()

#Decreasing number pattern
n=int(input("enter n:"))
a=1
for i in range(n+1,1,-1):
    for j in range(i-1):
        print((a+j),end='')
    print()

#Continuous number triangle
n=int(input("enter n:"))
a=1
for i in range(1,n+1):
    for j in range(i):
        
        print(a,end='')
        a+=1
    print() 

n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(n-i):
        print("*",end='')
    print()
# pyramid
n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(1,i+1):
         print("*",end=' ')
    for l in range(2,i+1):
        print("*",end=' ')
    print()
# inverse pyramid
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    for k in range(2,i+1):
        print("*",end=' ')
    print()        
# dymond partten
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(1,i+1):
         print("*",end=' ')
    for l in range(2,i+1):
        print("*",end=' ')
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    for k in range(2,i+1):
        print("*",end=' ')
    print()  

#number pyramid
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    for k in range(i-1,0,-1):
        print(k,end=' ')
    print()  
# holo square
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==n or i==1 or j==1:
         print("*",end=' ')
        else:
           print(" ",end=' ') 
    print()      

# holo right triangle
n=6
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==n or j==1 or j==i:
         print("*",end=' ') 
        else:
         print(" ",end=' ')
    print()   
# holo pyramid                                      
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(1,i+1):
        if   i==1 or k==1 or i==n  :
         print("*",end=' ')
        else:
         print(" ",end=' ')
    for k in range(2,i+1):
        if i==1 or i==n or k==i:
         print("*",end=' ')
        else:
         print(" ",end=' ')
    print()        
# continuous alphabet
a=65
for i in range(1,5):
    for j in range(i):
        print(chr(a+j),end=' ')
        a+=1
    print() 
# mirrored triangle
n=5 
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    print()           
# Sandglass pattern   
n=5 
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    print()  
for i in range(2,n+1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    print()     