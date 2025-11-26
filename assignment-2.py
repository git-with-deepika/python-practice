# print 1 to n
n=int(input("enter n:"))
for i in range(1,n):
    print(i,end=' ')
# sum of 1 to n
n=int(input("enter n:"))
sum=0
for i in range(1,n):
    sum=sum+i
    print(f'after adding{i} sum is {sum}')

# sum of 1 to n of even no.
n=int(input("enter n:"))
sum=0
for i in range(1,n):
    if i%2==0:
      sum=sum+i
    print(f'after adding{i} sum is {sum}')


# sum of 1 to n of odd no.
n=int(input("enter n:"))
sum=0
for i in range(1,n):
    if i%2!=0:
      sum=sum+i
    print(f'after adding{i} sum is {sum}')


# multiplacation table
n=int(input("enter n:"))
prod=1
i=1
for i in range(1,10+1):
    prod=n*i
    print(n,"*",i,"=",prod)
    i+=1

# count of digit
n=int(input("enter n:"))
count=0
sum=0
while n>0:
    sum=sum+n%10
    count+=1
    n=n//10
    print(count)
  
  # sum of digit
n=int(input("enter n:"))
count=0
sum=0
while n>0:
    sum=sum+n%10
    count+=1
    n=n//10
    print(sum)

# reverse a number
n=int(input("enter n:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    print(rev)
    n=n//10
    
#palindrom number

n=int(input("enter n:"))
rev=0
x=n
while n>0:
    rev= (rev*10)+n%10
    n=n//10

if x==rev:
        print("number is palindron")
else:
        print("number is not palindron")

#product of digit
n=int(input("enter n:"))
prod=1

while n>0:
    prod=prod*n%10
    print(prod)
    n=n//10

#factorial of a number 
n=int(input("enter n:"))
fact=1
for i in range(n,1,-1):
    fact=fact*i
    print(fact)

# take a number and print its all diviser
n=int(input("enter n:"))
print("divisiors are:")
for i in range(1,n+1):
  if n%i==0:
    print(i)
    i+=1
#check number is prime or not
n=int(input("enter n:"))
if n>1:
    for i in range(2,n):
     if n%i==0:
        print("number is not prime")
        break
     else:
        print("number is prime")   
else:
   print("number is not prime")    

# check a b number is divisible by 2 3:
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

print(f"Numbers between {a} and {b} divisible by both 2 and 3 are:")

for i in range(a + 1, b):
    if i % 6 == 0:
        print(i)

# sum of all prime number upto n    
    



# count of even and odd digits
n=int(input("enter n:"))
count_even=0
count_odd=0
for i in str(n):
    if int(i)%2==0:
     count_even+=1  
    else:     
        count_odd+=1 

print("even:",count_even)
print("odd:",count_odd)


    


# the sum of squares of the first n natural numbers
n=int(input("enter n:"))
sum=0
for i in range(1,n+1):
      i=i*i
      sum=sum+i
      print(sum)
      i+=1

#the sum of cube of the first n natural numbers
n=int(input("enter n:"))
cube=0
for i in range(1,n+1):
      i=i**3
      cube=cube+i
      print(cube)
      i+=1

# check weater a number is strong or not
n=int(input("enter n:"))
temp=n
sum=0
while n>0:
    digit=n%10
    fact=1
    print("digit:",digit)
    for i in range(1,digit+1):
     fact=fact*i
    print("factorial:",fact)
    sum=sum+fact
    print("sum:",sum)
    n=n//10
if temp==sum:
   print(temp," is strong number")
else:
    print(temp," is not a strong number")

# check armstrong number
n=int(input("enter n:"))
x=n
y=n
count=0
while n>0:
    digit=n%10
    count+=1
    print("count:",count)
    n=n//10
sum=0
while x>0:
    digit=x%10
    sum=sum+(digit**count)
    print("sum:",sum)
    x=x//10
if y==sum:
    print(y,"is a armstrong number")
else:
    print(y,"is not a armstrong number")    

    


      
