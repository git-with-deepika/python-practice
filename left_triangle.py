# *
# * *
# * * *
# * * * *
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    


# 1  
# 1 2
# 1 2 3
# 1 2 3 4
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#1
#2 2
#3 3 3
#4 4 4 4
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print() 


#1
#2 3
#4 5 6
#7 8 9 10
n=5
a=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end=" ")
        a+=1
    print() 
#2 
#4 6 8
#10 12 14 16
#18 20 22 24 26
n=5
a=2
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end=" ")
        a+=2
    print() 

#1
#3 5 7
#9 11 13 15
#17 19 21 23 25
n=5
a=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end=" ")
        a+=2
    print()
#20
#18 16 
#14 12 10
# 8 6 4 2

n=4
temp=n*(n+1)
for i in range(1,n+1):
    for j in range(1,i+1):
        print(temp,end=" ")
        temp-=2
    print()

# 19
# 17 15
# 13 11 9
# 7 5 3 1
n=4
temp=(n*(n+1))-1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(temp,end=" ")
        temp-=2
    print()


#* 
#* *
#*   *
#* * * *
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  
#*
#**
#***
#****
# one another option
for i in range(4):
    for j in range(4):
        if j <= i:
            print("*", end="")
        else:
            print(" ", end="")
    print()    

