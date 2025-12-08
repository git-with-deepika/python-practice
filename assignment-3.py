#level-1 :-

#print from 1 to 10
for i in range(1,11):
    print(i,end=' ')

# print even number from 1 to 20
for i in range(1,21):
    if i%2==0:
        print(i,end=' ')

 # print odd number from 1 to 20  
for i in range(1,21):
    if i%2!=0:
        print(i,end=' ')

#print squre of numbers from 1 to 10
for i in range(1,11):
    print(i*i,end=' ')
    i+=1    
#print hello 5 time
a=5
while a>0:
    print("hello")
    a-=1

for i in range(1,6):
    print("hello")
    i+=1
#level 2:-
#print number from 10 to 1
for i in range(10,0,-1):
    print(i,end=' ')

#print number from 1 to 50 divisible by 5
for i in range(1,51):
    if i%5==0:
        print(i,end=' ')

#print sum of 10 natural number
sum=0
for i in range(1,11):
    sum=sum+i
    
    print(f"After adding {i},sum is {sum}")

#product of 5 natural number
prod=1
for i in range(1,6):
    prod=prod*i
    
    print(f"After multing {i},product is {prod}")

#take a number from user and print 1 to number
n=int(input("enter number: "))
for i in range(1,n+1):
    print(i)
    i+=1

 #level 3:-
n=1
while n<=10:
    print(n,end=' ')
    n+=1 
#sum of digit entered by user or given
n=1234
sum=0
while n!=0:
    sum=sum+n%10
    print(sum)
    n=n//10
  # reverse 123 to 321
n=123
rev=0  
while n!=0:
    digit=n%10  
    rev=rev*10+digit
    print(rev)
    n=n//10   

#take user input number and print its table
n=int(input("enter number"))
i=1
mul=1
while i<=10:
    mul=n*i
    print(mul)
    i=i+1

# factorial of a number
n=6
fact=1
while n!=0:
    fact=fact*n
    print(fact)
    n-=1   

#partten
for i in range(1,5):
    for j in range(i):
        print('*',end=' ')
    print()

print()
for i in range(6,1,-1):
    for j in range(i-1):
        print('*',end=' ')
    print()

a=1
for i in range(1,5):
    for j in range(i):
        print(a+j,end=' ')
    print()



#prime number
n=int(input("enter number: "))

if n>1:
    for i in range(2,n):
        if n%1==0:
         print(n,"not a prime nuber")
         break
        else:
           print(n, "is a prime number")
else:
   print(n, "not a prime number")        

# print 1 to 100 and skip numner which is divisible by 3 by using countinue   
for i in range(1,101):
    if i%3==0:
        continue
    print(i,end=' ')


 


