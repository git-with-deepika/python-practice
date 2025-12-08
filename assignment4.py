
## IF -ELSE QUESTIONS
# check number is positive negative or zero
num=float(input("enter num:"))
if num >0:
    print("positive number")
elif num==0:
    print(" number zero")
else:
    print("number is negative")

# check even or odd
num= int(input("enter num:"))
if num %2==0:
    print("even number")
else:
    print("odd number")    

# check person is eligible to vote or not
age =int(input("enter age:"))
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
# largest of two numbers
a=int(input("enter a:"))
b= int(input("enter b:"))
if a >b:
    print("a is greatr")
else:
    print("b is greater")
# chech character is vowel or consonant
ch=input("enter character:")

if ch == 'a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("vowel")
else:
    print("consonant")    
 #chech number is divisible by 5 and 11
a=int(input("enter a:"))
if a%5==0 and a%11==0:
    print("a is divisible by 5 and 11")
else:   
    print("a is not divisible by 5 and 11")

# check leap year    
year=int(input("enter year:"))
if year %4==0 and(year %100 !=0 or year%400==0):
    print("leap year")
else:
    print("not a leap year")

## NESTED IF -ELSE QUESTIONS
num=int(input("enter num:"))
if num==0:
    print("number is zero")
elif num >0:
    print("number is positive")
    if num %2==0:
        (print("number is even"))
    else:
        print("number is odd")
else:
    print("number is negative")

# grade
marks=float(input("enter marks:"))
if marks >=90 and marks <=100:
    print("Grade A")
elif marks >=80 and marks <=90:
    print("Grade B")
elif marks >=70 and marks <=80:
    print("grade C")
elif marks >=60 and marks <=70:
    print("grade D")
else:
    print("fail")  

# check person is child trrn adult or senior
age =int(input("enter age:")) 
if age <=12:
    print("child") 
elif age <= 19:
    print("teenager")
elif age <=59:
    print("adult")     
else:
    print("srnior")  

# largest of three numbers 
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
if num1 > num2 and num1 > num3:
    print("largest number is:", num1)
elif num2 > num1 and num2 > num3:
    print("largest number is:", num2)    
else:
    print("largest number is:", num3)

# type of triangle
a=int(input("enter side a:"))
b= int(input("enter side b:"))
c= int(input("enter side c:"))
if a+b >c and b+c >a and c+a >b:
    if a==b and b==c:
        print("equilateral triangle")
    elif a==b or b==c or c==a:
        print("isosceles triangle")
    else:
        print("scalene triangle")
else:   
    print("not a triangle")


# FOR LOOP QUESTIONS
# print 1 to 100
for i in range(1,101):
    print(i,end=' ')

# print table 
num= int (input("enter num:"))
for i in range(1,10+1):
    print(f"{num}*{i}={num*i}")    

# sum of 10 natural number
num=int(input("enter num:"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print("sum is:",sum)

# even number 1 to 50
for i in range(1,51):
    if i%2==0:
        print(i,end=' ')

# factorial of a number
a=int(input("enter a:")) 
fact=1
for i in range(a,1,-1):
    fact=fact*i
print(fact)      
#fabonacci series
n=int(input("enter n:")) 
a=0
b=1
for i in range(n):
    print(a,end=' ')
    c=a+b
    b=a
    a=c
    
# number is prime or not
n=int(input("enter n:"))    
if n>1:
    for i in range (2,n):
        if n%i==0:
         print("number is not prime")
         break
    else:
         print("number is prime")
# count number of digit
n=int(input("enter n:"))
count=0
for i in  str(n):
    count+=1
print("number of digit is:",count)

#sum of digit 
n=int(input("enter n:"))
sum=0
for i in range(n):
    digit=n%10
    sum=sum+digit
    n=n//10
print("sum of digit is:",sum)
# LCM of two numbers
a=int(input("enter a:"))
b=int(input("enter b:"))
greater=max(a,b)
for i in range(1,(a*b)+1):
    if i%a==0 and i%b==0:
        lcm=i
        break
print("LCM is:",lcm)
    
#WHILE LOOP QUESTIONS
# print 1 to 10
num=1
while num <=10:
    print(num,end=" ")
    num+=1
# reverse a number
n=int(input("enter n"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10 +digit
    n=n//10
    print(rev)
# palindrome number
n=int(input("enter n"))
rev=0
x=n
while n>0:
    digit=n%10
    rev=rev*10 +digit
    n=n//10
    print(rev)    
if x== rev:
    print("palindrome number")
else:
    print("not a palindrome number")
                
# take input untill 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Program ended.")
        break
    else:
        print(f"You entered: {num}")

# HCF
a=int(input("enter a:"))
b=int(input("enter b:"))
while b!=0:
    a , b= b, a%b
print("HCF is:",a)

# odd numbers beteen 2 numbers
a=int(input("enter a:"))
b=int(input("enter b:"))
while a<=b:
    if a%2 !=0:
     print("odd numbers are:",a,end=' ')
    a+=1


# miltiplication of table
a=int(input("enter a:"))
i=1
while i<=10:
   print(f"{a} *{i}={a*i}")
   i+=1

# sum of digit
num=int(input("enter num:"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
    print("sum of digit is:",sum)

#fabonacci series
num=int(input("enter num:"))
a=0
b=1
while num>0:
    print(a,end=' ')
    c=a+b
    a=b
    b=c
    num-=1
