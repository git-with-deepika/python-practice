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

# 16. Write a function to check whether a string is a palindrome.
st=input("enter string...")
st1=st
new_st=''
def check_palindrome(st,st1,new_st):
    for ch in st:
        new_st=ch+new_st
    if new_st == st:
        return "the string is palindrome" 
    else:
        return "the string is not palindrome"

palindrome=check_palindrome(st,st1,new_st)
print(palindrome)       

# 17. Write a function that returns the nth Fibonacci number using loops.

n=int(input("enter number.."))  
def fabonacci(n):
    a=0
    b=1
    result=[]
    for i in range(n):
        result.append(a)
        a , b = b , a+b
    return result

check=fabonacci(n)   
print(check)            

# 18. Write a function that swaps two numbers without using a third variable.
a=int(input(" first value before swap..."))
b=int(input(" second value  before swap..."))
def swap(a,b):
    b=a+b
    a=b-a
    b=b-a
    return a,b

na,nb=swap(a,b)
print(f'first value after swap {na} , second value after swap {nb}')   

# 19. Write a function that returns whether a year is a leap year.
year=int(input("enter year :"))
def check_year(year):
    if (year%4==0 ) or (year%100 != 0 and year%400==0):
        return f'{year} is a leap year'
    else:
        return f'{year} is  not a leap year'
    
leap_year=check_year(year)
print(leap_year)              

# 20. Write a function that converts Celsius to Fahrenheit.
celsius=int(input("enter celcius...."))
def cel_to_fahr(celsius):
    return (celsius * 9/5)+32

fahrenheit=cel_to_fahr(celsius)
print(fahrenheit)              

# type 2nd

# in list 
li=[20,45,43,33]
new=[]
def temp(t):
    f= (t*9/5)+32
    return f

for element in li:
    new_li=temp(element)
    new.append(new_li)
print(new)    


# 21. Write a function that counts how many times a function is called.
count=0
def my_function():
    global count
    count+=1
    print(f'function called {count} time')

my_function()  
my_function()  


# 22. Write a function that returns another function.
def outer():
    def inner():
        return 'hello this is inner function'
    return inner 

new_fun=outer()
print(new_fun())


# 23. Write a function that takes another function as an argument and executes it.
def new(func,a,b):
    return func(a,b) 

def add (x,y):
    return x+y

new_result=new(add,3,4)
print(new_result)   

# 24. Write a lambda function to find the square of a number.

def result(fun,x):
    return fun(x)

def square(x):
    return x*x

new_squ=result(square,3)
print(new_squ)                    

#25. Write a lambda function to find the maximum of two numbers.
maximum=lambda x,y : x if x > y else y
print(maximum(3,4))                
   
# 26. Write a function to calculate the power of a number (a^b).
a=int(input("entr number.."))
b=int(input("entr number.."))
def power(a,b):
    result=1
    for i in range(b):
        result*=a
    return result

new_result=power(a,b)
print(new_result)    

# 27. Write a function to find the sum of digits of a number.
num=int(input("enter number of digit.."))
def number(num):
    sum=0
    digit=0
    while num >0:
        digit=num%10
        sum+=digit
        num=num//10
    return sum

new_sum=number(num)
print(new_sum)    
# 28. Write a function that checks whether all arguments passed are positive numbers.

num=list(map(int,input("enter list of numbers..").split()))
def all_positive(*args):
    for i in args:
        if i <= 0:
            return False
    return True

result=all_positive(*num)
print(result)                 

# 29. Write a function that returns multiple values (sum, difference, product) of two numbers.
def sum(a,b):
    return a+b

def diff(a,b):
    return a-b

def prod(a,b):
    return a*b

def all_op(sum,diff,prod):
    a=int(input("enter number.."))
    b=int(input("enter number.."))
    opr=input("enter operator..")         

# 30. Write a function that prints a pattern using only function calls.
n=int(input("enter n: "))
def partten(n,row=1):
    if row <= n:
        line="*" *row
        return line + '\n' + partten(n,row+1)
    else:
        return " "
    
new_partten=partten(n,row=1)
print(new_partten)   

# inverted triangle

def print_star(n):
    if n>0:
        print("*"*n)
        print_star(n-1)

print_star(4)     

# 31. Write a function to calculate the average of numbers using *args.
num=list(map(int,input("enter number :").split()))
def avg(*args):
    sum=0
    count=0
    av=0
    for element in args:
        sum+=element
        count+=1
        av=sum/count
    return av

new_avg=avg(*num)
print(f'the average is {new_avg}')    

# 32. Write a function to merge two dictionaries using **kwargs.
def merge_dict(**kwargs):
    merge={}
    for element in kwargs.values():
        merge.update(element)
    return merge

dict1={'a':1,'b':2}
dict2={'c':3,'d':4}

new_dict=merge_dict(first=dict1,second=dict2)
print("new dictionary is :",new_dict)              

# 33. Write a function that demonstrates local and global variable behavior.
x=20
def demo_fun():
    y=5
    print("inside the function global variable is :",x)
    print("inside the function the lical variable is: ",y)

def modify_variable():
    global x
    x=10
    print("inside the function the global variable after change :",x)

demo_fun()
print("outside the function the global variable is: ",x)

modify_variable()
print("outside the function the gobal variable after change: ",x)   

# 34. Write a function that accepts another function and applies it to a value.
def apply(fun,value):
    return fun(value)

def square(x):
    return x*x

accept=apply(square,3)
print("the square is :",accept)  

# 35. Write a function to generate a multiplication table of a number.
n=int(input("enter number for table :"))
def table(n):
    result=''
    for i in range(1,11):
        result += f'{n}*{i} = {n*i}\n'
    return result
    
tbl=table(n)
print(tbl)          

# 36. Write a function to check whether a number is Armstrong or not.
def is_armstrong(num):
    # Convert number to string to easily iterate over digits
    digits = str(num)
    n = len(digits)  # number of digits
    
    # Calculate sum of each digit raised to the power n
    total = sum(int(digit) ** n for digit in digits)
    
    # Check if equal to original number
    return total == num

# Example usage:
print(is_armstrong(153))   # True
print(is_armstrong(9474))  # True
print(is_armstrong(123))   # False   



# 37. Write a function that validates a password based on given rules.
import re

def validate_password(password):
    # Rule 1: Minimum length 8
    if len(password) < 8:
        return False
    
    # Rule 2: At least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False
    
    # Rule 3: At least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False
    
    # Rule 4: At least one digit
    if not re.search(r"[0-9]", password):
        return False
    
    # Rule 5: At least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    
    return True

# Example usage:
print(validate_password("StrongPass1!"))  # True
print(validate_password("weakpass"))      # False
print(validate_password("NoDigits!"))     # False


# 38. Write a function to count words in a sentence.
st='wkeakfl'
def count_word(st):
    count=0
    for ch in st:
        count+=1
    return count

count=count_word(st) 
print(count)   

# 39. Write a function to remove duplicates from a list.
li=[2,3,3,4,5,5,6,7]
new=[]
def re_duplicate(li):
    for element in li:
        if element not in new:
            new.append(element)
    return new

new_list=re_duplicate(li)    
print(new_list)    

    
# 40. Write a function to check whether two strings are anagrams.
# method 1

st1='pen'
st2='nep'
def is_anagram(st1,st2):
    for ch in st1:
        return " is anagram"
    else:
        return 'not anagram'
    
new=is_anagram(st1,st2)
print(new)    
 # method 2
st='nep'
st3='pen'
is_anagram=True

def check(st,st3):
    for ch in st:
        if ch not in st3:
            is_anagram = False
            break
    return True 

new_check=check(st,st3)
print(new_check)             
           

                    # Theory Questions up to the functions

'''41. Why is Python called a high-level language?
Python is called a high-level language because it is easy to read, write, and understand, and it hides hardware-level details from the programmer.
42. What are the key features of Python?
Simple syntax, interpreted, high-level, dynamically typed, object-oriented, portable, and a large standard library.
43. Is Python case-sensitive?
Yes, Python is case-sensitive.
44. What is the difference between Python 2 and Python 3?
Python 3 supports Unicode by default, uses print() as a function, has better integer division, and Python 2 is no longer supported.
45. What is an interpreter?
An interpreter executes code line by line without compiling it first.
46. How does Python execute code?
Python converts source code into bytecode and executes it using the Python Virtual Machine (PVM).
47. What is dynamic typing?
In dynamic typing, variable data types are decided at runtime, not before execution.
48. What is strong typing in Python?
Python does not allow operations between incompatible data types without explicit conversion.
49. What is a variable?
A variable is a name that stores a value in memory.
50. How are variables created in Python?
Variables are created by assigning a value using the assignment operator (=).
51. What are naming rules for variables?
They must start with a letter or underscore, cannot start with a digit, cannot be keywords, no spaces, and are case-sensitive.
52. What are keywords in Python?
Keywords are reserved words that have special meaning in Python.
53. How can you see all Python keywords?
Using the keyword module: keyword.kwlist.
54. What is memory management in Python?
Python automatically handles memory allocation and deallocation.
55. What is garbage collection?
Garbage collection removes unused objects from memory automatically.
56. What is indentation in Python?
Indentation refers to the spaces used to define blocks of code.
57. Why is indentation important?
Indentation defines code structure and is mandatory in Python.
58. What is a comment?
A comment is used to explain code and is not executed.
59. Difference between single-line and multi-line comments.
Single-line comments use #; multi-line comments use triple quotes.
60. What is an expression?
An expression is a combination of values and operators that returns a value.
61. What is a statement?
A statement is an instruction that performs an action.
62. Difference between expression and statement.
An expression returns a value, while a statement performs an action.
63. What are literals in Python?
Literals are fixed values like numbers, strings, and booleans.
64. What are data types?
Data types define the type of data a variable can store.
65. How many built-in data types are there?
Main categories include Numeric, Sequence, Set, Mapping, Boolean, and NoneType.
66. What is type() function?
The type() function returns the data type of a variable.
67. What is type casting?
Type casting is converting one data type into another.
68. Difference between implicit and explicit type casting.
Implicit is done automatically by Python; explicit is done by the programmer.
69. What is input() function?
The input() function takes input from the user.
70. What does input() return by default?
It returns a string.
71. Difference between print() and input().
print() displays output; input() takes input.
72. What are operators?
Operators are symbols used to perform operations.
73. Types of operators in Python.
Arithmetic, Relational, Logical, Assignment, Bitwise, Identity, and Membership.
74. Difference between = and ==.
= assigns a value; == compares values.
75. Difference between is and ==.
is checks memory location; == checks value equality.
76. What are relational operators?
Operators used to compare values like >, <, ==, !=.
77. What are logical operators?
Logical operators are and, or, and not.
78. What is short-circuiting in logical operators?
Evaluation stops as soon as the result is determined.
79. What are bitwise operators?
Operators that work on bits, such as &, |, ^, ~.
80. What is a conditional statement?
A statement used to make decisions based on conditions.
81. What is if statement?
Executes code when a condition is true.
82. What is elif?
Used to check multiple conditions.
83. What is else?
Executes when all conditions are false.
84. Can if exist without else?
Yes, an if statement can exist without else.
85. What is nested if?
An if statement inside another if statement.
86. What is a loop?
A loop is used to repeat a block of code.
87. Why are loops used?
To avoid writing repetitive code.
88. What is a for loop?
Used to iterate over a sequence.
89. What is a while loop?
Runs as long as a condition is true.
90. Difference between for and while loop.
For loop is used for known iterations; while loop is condition-based.
91. What is infinite loop?
A loop that never ends.
92. What is break statement?
Stops the loop immediately.
93. What is continue statement?
Skips the current iteration.
94. What is pass statement?
A placeholder that does nothing.
95. What is range() function?
Generates a sequence of numbers.
96. What does range(1, 10, 2) produce?
1, 3, 5, 7, 9
97. Can range() be used in while loop?
Not directly; it is commonly used with a counter.
98. What is loop else?
An else block associated with a loop.
99. When does loop else execute?
When the loop completes normally without a break.
100. What is a function?
A reusable block of code.
101. Why do we use functions?
For code reusability, readability, and modularity.
102. How do you define a function?
Using the def keyword.
103. What is the syntax of a function?
def function_name():
104. What is function calling?
Executing a function.
105. Difference between defining and calling a function.
Defining creates the function; calling executes it.
106. What are parameters?
Variables defined in the function definition.
107. What are arguments?
Values passed during function call.
108. Difference between parameters and arguments.
Parameters receive values; arguments send values.
109. What is a return statement?
Used to send a value back from a function.
110. Can a function return multiple values?
Yes, using tuples.
111. What happens if a function has no return?
It returns None.
112. What is default parameter?
A parameter with a predefined value.
113. How do default arguments work?
Default value is used if no argument is provided.
114. What are positional arguments?
Arguments passed in order.
115. What are keyword arguments?
Arguments passed using parameter names.
*116. What is args?
Used to accept multiple positional arguments.
*117. Why is args used?
To handle variable number of arguments.
**118. What is kwargs?
Used to accept multiple keyword arguments.
**119. Why is kwargs used?
To pass key-value pair arguments.
**120. Can we use both *args and kwargs together?
Yes.
121. What is variable scope?
The area where a variable is accessible.
122. What is local scope?
Scope inside a function.
123. What is global scope?
Scope outside all functions.
124. Difference between local and global variables.
Local variables exist inside functions; global variables exist throughout the program.
125. What is the global keyword?
Used to modify a global variable inside a function.
126. Why do we need global keyword?
To change global variables from within a function.
127. Can a function access a global variable?
Yes.
128. Can a function modify a global variable?
Yes, using the global keyword.
129. What is nested function?
A function defined inside another function.
130. Can we define a function inside another function?
Yes.
131. What is function recursion?
A function calling itself.
132. What is base condition in recursion?
The condition that stops recursion.
133. What happens if base condition is missing?
It leads to infinite recursion and error.
134. What is stack overflow?
Error caused by excessive recursive calls.
135. What is lambda function?
An anonymous one-line function.
136. Difference between lambda and normal function.
Lambda is short and single-expression; normal functions are multi-line.
137. Can a function be assigned to a variable?
Yes.
138. What is a first-class function?
A function that can be stored, passed, and returned like a value.
139. What is a higher-order function?
A function that takes another function as an argument or returns a function.  '''

             






    




    
     
    
         

        

    
        




