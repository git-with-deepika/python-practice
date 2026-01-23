#           Functions Assignment
#1. Write a function to add two numbers and return the result.
a=int(input("enter first number.."))
b=int(input("enter second number..."))
def add(a,b):
    return a+b
sum=add(a,b)
print(f'the sum of {a} and {b} is :',sum) 

# 2. Write a function that takes a number and returns its square.
a=int(input("enter number.."))
def square(a):
    return a*a
a_square=square(a)
print(f'the square of {a} is :',a_square)  

# 3. Write a function to check whether a number is even or odd.
a=int(input("enter number.."))
def check_no(a):
    if a%2==0:
        return f'the {a} is even number'
    else:
        return f'the {a} is odd number'
    
number=check_no(a)
print(number)    

# 4. Write a function to find the maximum of three numbers.
a=int(input("enter first number.."))
b=int(input("enter second number..."))
c=int(input("enter third number.."))
def max_num(a,b,c):
    if a > b and a > c:
        return f'{a} is maximum number'
    elif b > a and b >c :
        return f'{b} is maximum number'
    else:
        return f'{c} is maximum number'
    
maximum=max_num(a,b,c)
print(maximum)    

# 5. Write a function to calculate the factorial of a number (without recursion).
a=int(input("enter number.."))

def fact(a):
    factorial=1
    for i in range(1,a+1):
        factorial*=i
    return factorial
new_fact=fact(a)    
print(new_fact)   

# 6. Write a function to check whether a number is prime.
a=int(input("enter number.."))
def is_prime(a):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    if count==2:
        return f'{a} is a prime number ' 
    else:
        return f'{a} is a not prime number ' 
           
check_prime=is_prime(a)
print(check_prime)  

# 7. Write a function to return the sum of all numbers in a given list.
li=list(map(int,input("enter number of list :").split()))
def list_sum(li):
    sum=0
    for element in li:
        sum+=element
    return sum
li_sum=list_sum(li)
print(f'the sum of list is :',li_sum)    

# 8. Write a function to count the number of digits in a number.
a=int(input("enter number :"))
def check(a):
    count=0
    sum=0
    while a >0:
        sum=sum+a%10
        count+=1
        a=a//10
    return count     
check_no=check(a)
print(check_no)    

# 9. Write a function to reverse a number.
a=int(input("enter number :"))
def reverse(a):
    digit=0
    rev=0
    while a >0:
        digit=a%10
        rev=rev*10+digit
        a=a//10
    return rev
new_rev=reverse(a)
print(new_rev)        

# 10. Write a function to reverse a string.
st=input("enter string....")
def st_reverse(a):
    revr=''
    for i in st:
        revr=i+revr
    return revr
new=st_reverse(st)
print(new)    

# 11. Write a function to count vowels in a string.
s=input("enter string...")
vowel="aeiouAEIOU"
def check(s,vowel):
    count=0
    for i in vowel:
        if i in s:
            count+=1
    return count
value=check(s,vowel)
print(value)           

# 12. Write a function that returns both the minimum and maximum from a list.
li=[23,54,55,76,45,78]
def max_min(li):
    max_num=li[0]
    min_num=li[0]
    for element in li:
        if element > max_num :
            max_num=element
        if element < min_num:
            min_num=element
    return max_num,min_num

mx,mn=max_min(li)
print("maximum number is :",mx)  
print("minimum  number is :",mn)       

# 13. Write a function using default arguments to calculate simple interest.
p=int(input("enter principal amount.."))
r=int(input("enter rate of interest.."))
t=int(input("enter time..."))
def simple_interest(p,r,t):
    return (p*r*t)/100

new_interest=simple_interest(p,r,t)
print(new_interest)           

# 14. Write a function that accepts any number of arguments and returns their sum using *args.
num=list(map(int,input("enter number...").split()))
def add(*args):
    sum=0
    for element in args:
        sum+=element
    return sum
result=add(*num)
print(f'the sum is {result}')    

# 15. Write a function that accepts key-value pairs using **kwargs and prints them in formatted form.
def detail(**kwargs):
    for key , value in kwargs.items():
        print(f'key-> {key} : value-> {value}')
    return kwargs

detail(name='deepika',location='jaipur',batch='a23')    

       

        

    
        




