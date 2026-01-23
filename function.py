# function :- function is the block of reusable code whenever their is need of that code we call that function
# on the time of function defining we give the parameter which are being used into the function 
# def keyword is used to define the function 
# (parameter):- def function_name (parameter):
#                       particular task

def coffee_machine(suger,milk,beans):
    #prepare beans
    print("preparing beans")
    # taking milk 
    print("mixing coffe with the milk")
    #coffe is ready
    print("your coffee is ready")
# calling function :- at the time of cslling function with the function name we pass the values
# at that and that values are knoem=n as arguments
coffee_machine('suger','milk','beans')

def add(a,b):
    # return keyword is used to return the value
    return a+b
# when we are calling the function this returns a value....stored into the variable
# whch we can use anywhere in oue program
sum=add(3,4)
print(sum)


# calculator function
a=int(input("enter  first number :"))
b=int(input("enter  second number :"))
opr=input("enter operator like +,-,*..")
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub (a,b):
    return a-b
def divi (a,b):
    return a//b

if opr=='+':
    sum=add(a,b)
    print("sum is :",sum)
elif opr=='*':
    mult=mul(a,b)
    print("multiplication is :",mult)
elif opr=='-':
    subt=sub(a,b)
    print("subtraction is :",subt)
elif opr=='//':
    div=divi(a,b)
    print("division is :",div)
else:
    print('enter a valid operator...')    

def greeting(name):
      return f'Hello {name} how may i help you'

name=input("enter your name: ")
message = greeting(name)
print(f'Ui, {message}')
print(f'dashboard,{message}')


# default argument : into this argument we basically pass default value with parameter
def greeting(name='user'):
  return f'Hello {name} how may i help you'

name=input("enter your name: ")
message = greeting(name)
print(f'Ui, {message}')
print(f'dashboard,{message}')

# positional arguments are which are the passed at the function calling in that position in which the parameters are defined


# keyword argument: at the time of calling function we pass values with parameters name-> location -> 'valuef
def show_details(name,location):
  return f'hello i am {name} . anf i belongs from {location}'

name=input("enter your name: ")
location=input("enter your location: ")
show_details(location=location,name=name)


def student_details(name,age,city):
      return f'hello i am {name} and my age is {age} and i am from {city}'

name=input("enter your name: ")
age=input("enter your age: ")
city=input("enter your city: ")
student_details(name=name,city=city,age=age)


def employee_details(name,depart,sal):
      return f'employee name is {name} and her/his department is {depart} and her/him salary is {sal}'

employee_details('deepika','aws',21000)


def employee_details(name,depart,sal):
      return f'Employee name is {name} and Department is-> {depart} and the Salary is-> {sal}'
name=input("enter name: ")
depart=input("enter your department: ")
sal=int(input("enter your salary: "))

def employee_details(name,depart,sal):
      return f'employee name is {name} and her/his department is {depart} and her/him salary is {sal}'

employee_details(name='deepika',depart='aws',sal='50')

# golbal variable : which is accessable inside or outside the function you can use  this variable anywhere into the program
# if you want to the value of the global var then you use the 'global' kryword to access that variable

var=1
def count():
  # local variable is only acessable inside the function we can't use it outside the  the function
  var1=2
  global var
  var=20

count()
print(var)

#############   HIGHER ORDER FUNCTION 
# higher order functions are the functions that take a function as an argument or return that function
# higher orde function are the functions are the functions which is used to call another function as an parameter
# into the higher order function we basically pass other function as an another function


def hello(fun):
     print('hello from hello function ')
     # here we have called the another function
     fun()
def fun():
     print("hello from nested function")   
     # here we have passed the anothe rfunction as an argument

print(hello(fun))  


# calculator function

def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub (a,b):
    return a-b
def divi (a,b):
    return a//b

def calculator(add, mul , sub, divi):
     a=int(input("enter  first number :"))
     b=int(input("enter  second number :"))
     opr=input("enter operator like +,-,*.... :")
     if opr=='+':
        sum=add(a,b)
        print("sum is :",sum)
     elif opr=='*':
      mult=mul(a,b)
      print("multiplication is :",mult)
     elif opr=='-':
      subt=sub(a,b)
      print("subtraction is :",subt)
     elif opr=='//':
      div=divi(a,b)
      print("division is :",div)
     else:
      print('enter a valid operator...') 
calculator(add, mul,sub,divi)   

#  another calculator function

def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub (a,b):
    return a-b
def divi (a,b):
    if b==0:
        return "division is not allowed by 0"
    return a//b

def cal(add,sub,mul,divi):
    a=int(input("enter  first number :"))
    b=int(input("enter  second number :"))
    opr=input("enter operator like +,-,*.... :")

    operator={
        '+':add,
        '-':sub,
        '*':mul,
        '//':divi
    }
    if opr in operator:
        result=operator[opr](a,b)
        print(f'the {opr} is : {result}')
    else:
        print("invalid operator...")

cal(add,sub,mul,divi)            

# WAP to define function inside function in which uoy pass 2 number and the inner function print the sum of two numbers and call into the outer function
def outer():
    def add(a,b):
        return a+b
    sum=add(3,4)
    print(sum)

outer()    

# if we want to pass value from outer function
def outer(a,b):
    def add(a,b):
        return a+b
    sum=add(a,b)
    print(sum)

outer(5,5) 

# agr hame value bahar bhi use krni h
def outer(a,b):
    def add(a,b):
        return a+b
    sum=add(a,b)
    return sum
result=outer(5,5)
print(result)  

# WAP to check number is even or not    ( method 1 by using HOF)
a=int(input("enter number: "))
def check(a):
  def even(a):
   if a%2==0:
    return f'{a} is even number'
   else:
    return f'{a} not a even number'

  new=even(a)
  return new 

result=check(a)
print(result)       

# WAP to check a number is prime or not  ( method 1 by using HOF)
num=int(input("enter number: "))

def is_check(num):
  def prime(num):
   for i in range(2,num):
    if num%i==0:
      return f'{num} is not a prime number'
      break
    else:
      return f'{num} is a prime number'  

  is_prime=prime(num) 
  return is_prime
result=is_check(num)
print(result)

#  WAP to reverse a list   ( method 1 by using HOF)
lis=list(map(int,input("enter list ::").split()))
def new_lis(lis):
  def rev_list(lis):
    rev=[]
    for i in range(len(lis)-1,-1,-1):
     rev.append(lis[i])
    return rev
  new=rev_list(lis)
  return new
result=new_lis(lis) 
print(result)

# WAP to check a number is prime or not
def is_prime(n):
  for i in range(2,n):
        if n%i==0:
          return False
  return True    
check_prime=is_prime(7)
if check_prime:
  print("prime number")
else:
  print("not a prime number" ) 

##  VARIABLE LENGTH ARGUMENTS
# variable length arguments are used to pass the variable length of the arguments either it could be 2 or more
# it returns all arguments in the tuple
def add(*args):
  sum=0
  for element in args:
        sum+=element
  return sum
add(1,2,3,4,5,6,7)     
## VARIABLEN LENGTH KEYWORD ARGUMENT
# in which we can pass key and value pairs as much we want variables . it returns the data in the form of dictionary
def details(**kwargs):
  for key ,value in kwargs.items():
        print(f'{key} -> {value}')
  return kwargs     
details(name='deepika',batch='a23',location='jaipur',)        
##### LAMBDA FUNCTION 

# lambda function :-  it's a function which is used into the python for one line function and it is defined
# or initialized using 'lambda' keyword
# it's a anonymous function which is defined using the lambda keyword

sum_1=lambda a,b:a+b # here we have stored lambda function in sum_1 variables
print(sum_1(3,4))

#  WAP to print the product of two number
prod=lambda a,b: a*b
print(prod(3,5))


# check number is even or odd
# syntax:- lambda a: 'even' if condition (true) else return_false
func=lambda a : 'even' if a%2==0 else 'odd'
print(func(10))


# WAP to check whether a number is negative or positive
num=lambda a:'posotive' if a >0 else 'negative'
print(num(4))

# WAP to check the eligibility for vote
vote=lambda age: 'eligible' if age >= 18 else 'not eligible'
print(vote(19))

# WAP to check wether the person will pass or fail
person=lambda marks : 'pass' if marks > 40 else 'fail'
print(person(45))  


######## MAP FUNCTION
# map:- map function is used to map all the element of the iterables with a function 
# the basic syntax of the map is :- map(fun,iterable)
li=[1,2,3,4]
new_list=[]
def squre(n):
     return n*n 
for element in li:
     sorted_li=squre(element)
     new_list.append(element)
print(new_list)

#using map
mapped_obj=list(map(squre,li))
print(mapped_obj)
mapped_obj1=list(map(lambda element: element **2,li))
print(mapped_obj1)


li=[1,2,3,4]
new_list=[]
def eve(n):
     if n%2==0:
            return "even"
     else:
            return "odd"
     
for element in li:
      new_li=eve(element)
      new_list.append(new_li)
print(new_list)           


even_no=list(map(eve,li))
print(even_no)
even_num=list(map(lambda element:"even" if element%2==0 else "odd",li))
print(even_num)

lis=[0,20,30,40]
new=[]

# (tem * 9/5) +32

def temp(t):
      return (t*9//5)+32

for element in lis:
      new_temp=temp(element)
      new.append(new_temp)
print(new)


new_map=list(map(temp,lis))
print(new_map)

new_temp_lam=list(map(lambda element : (element*9//5)+32,lis))
print(new_temp_lam)

###### FILTER FUNCTION
# filter(func,iterable)
li=[1,2,3,4,5,6,7,8,9]
num=list(filter(lambda element : element%2==0,li))
num2=list(filter(lambda element : element%2!=0,li))
print("even number: ",num)
print("odd number: ",num2)  