# 1. Print numbers from 1 to n using recursion.
def num(n):
    if n==11:
        return
    print(n)
    num(n+1)

num(1)
print(num)

# 2. Print numbers from n to 1 using recursion.
def num(n):
    if n==0:
        return
    print(n)
    num(n-1)

num(10)
print(num)

# 3. Find the sum of first n natural numbers using recursion.
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)

n=5
print(sum(n))

# 4. Find the factorial of a number using recursion.
def fact(n):
    if n==0:
        return 0
    result=n*(n-1)
    return result

new=fact(5)
print(new)

# 5. Find the power of a number a^b using recursion.
def pow(a,b):
    if b==0:
        return 1
    return a*pow(a,b-1)

new=pow(2,3)
print(new)

# 6. Find the sum of digits of a number using recursion.
def dig(n):
    if n==0:
        return 0

    return n%10+dig(n//10)

digit=dig(123)
print(digit)

# 7. Reverse a number using recursion.
def reverse(n,rev=0):
    if n==0:
        return rev
    else:
        digit=n%10
        rev=rev*10+digit
        return reverse(n//10,rev)

new_rev=reverse(123)
print(new_rev)

# 8. Check whether a number is a palindrome using recursion.
def is_palindrome_recursive(s):
    # Base case: empty string or single character
    if len(s) <= 1:
        return True

    # Compare first and last characters
    if s[0] != s[-1]:
        return False

    # Recursive call on the substring excluding first and last characters
    return is_palindrome_recursive(s[1:-1])

# Wrapper function for numbers
def is_palindrome_number(num):
    return is_palindrome_recursive(str(num))

# Example usage
print(is_palindrome_number(121))
print(is_palindrome_number(12321))


# Function call
if is_palindrome_number(num):
    print("Palindrome")
else:
    print("Not Palindrome")


# 9. Find the nth Fibonacci number using recursion.
def fabo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fabo(n-1)+fabo(n-2)


for i in range(10):
    print(fabo(i),end=' ')

# 11. Count the number of digits in a number using recursion.
def dig(n):
    if n==0:
        return 0
    return 1+dig(n//10)

digit=dig(123)
print(digit)

# 13. Check whether a string is a palindrome using recursion.
def is_palindrome(s):
    # Base case: empty string or single character
    if len(s) <= 1:
        return True
    # If first and last characters are not same
    if s[0] != s[-1]:
        return False
    # Recursive call
    return is_palindrome(s[1:-1])


# Input
text = input("Enter a string: ")

# 16. Find the sum of all elements in a list using recursion.
def recursive_sum(lst):

    if len(lst) == 0:
        return 0

    # first element + sum of rest
    return lst[0] + recursive_sum(lst[1:])

numbers = [1, 2, 3, 4, 5]
print("Sum of list:", recursive_sum(numbers))


#17. Find the maximum element in a list using recursion.
def recursive_max(lst):
    # Base case: if list has only one element
    if len(lst) == 1:
        return lst[0]

    # Recursive case: find max of rest of list
    max_rest = recursive_max(lst[1:])

    # Compare first element with max of rest
    return lst[0] if lst[0] > max_rest else max_rest


numbers = [3, 7, 2, 9, 5]
print("Maximum element:", recursive_max(numbers))

# 18. Find the minimum element in a list using recursion.
def recursive_min(lst):
    # Base case: if list has only one element
    if len(lst) == 1:
        return lst[0]

    # Recursive case: find min of rest of list
    min_rest = recursive_min(lst[1:])

    # Compare first element with min of rest
    return lst[0] if lst[0] < min_rest else min_rest


numbers = [8, 3, 10, 1, 6]
print("Minimum element:", recursive_min(numbers))

# 19. Check whether a number is even or odd using recursion.
def is_even_or_odd(n):
    # Handle negative numbers by converting to positive
    if n < 0:
        n = -n

    # Base cases
    if n == 0:
        return "Even"
    elif n == 1:
        return "Odd"

    # Recursive case
    return is_even_or_odd(n - 2)


print(is_even_or_odd(10))

# 20. Calculate GCD of two numbers using recursion.
def gcd(a, b):
    # Base case
    if b == 0:
        return a


    return gcd(b, a % b)


print("GCD of 48 and 18:", gcd(48, 18))


'''21. Why is Python called a high-level language?
Python is called a high-level language because it is easy to read, write, and understand. It hides complex hardware details and uses simple English-like syntax.
22. What are the key features of Python?
Python is simple, interpreted, high-level, dynamically typed, object-oriented, portable, and has a large standard library.
23. Is Python case-sensitive?
Yes, Python is case-sensitive. For example, Variable and variable are different.
24. What is the difference between Python 2 and Python 3?
Python 3 supports Unicode by default, better syntax, improved libraries, and enhanced security, while Python 2 is outdated and no longer supported.
25. What is an interpreter?
An interpreter is a program that executes code line by line instead of converting it into machine code all at once.
26. How does Python execute code?
Python first compiles code into bytecode and then executes it using the Python Virtual Machine (PVM).
27. What is dynamic typing?
Dynamic typing means you do not need to declare a variable’s data type; Python decides it at runtime.
28. What is strong typing in Python?
Strong typing means Python does not allow automatic conversion between incompatible data types.
29. What is a variable?
A variable is a name that refers to a value stored in memory.
30. How are variables created in Python?
Variables are created by assigning a value using the = operator.
31. What are naming rules for variables?
Variable names must start with a letter or underscore, cannot start with a number, cannot use keywords, and cannot contain spaces.
32. What are keywords in Python?
Keywords are reserved words that have special meanings in Python, such as if, else, and while.
33. How can you see all Python keywords?
By using the keyword module and keyword.kwlist.
34. What is memory management in Python?
Python automatically manages memory allocation and deallocation using a private heap.
35. What is garbage collection?
Garbage collection automatically removes unused objects from memory.
36. What is indentation in Python?
Indentation refers to spaces at the beginning of a line that define code blocks.
37. Why is indentation important?
Indentation is mandatory in Python because it defines the structure and logic of the program.
38. What is a comment?
A comment is text that is ignored by the interpreter and used to explain code.
39. Difference between single-line and multi-line comments.
Single-line comments use #. Multi-line comments use triple quotes (or ).
40. What is an expression?
An expression is a combination of values and operators that produces a result.
41. What is a statement?
A statement is a complete instruction that performs an action.
42. Difference between expression and statement.
An expression returns a value, while a statement performs an action.
43. What are literals in Python?
Literals are fixed values like numbers, strings, and booleans.
44. What are data types?
Data types define the kind of data a variable can hold.
45. How many built-in data types are there?
Python has several built-in types such as int, float, str, list, tuple, set, and dict.
46. What is type() function?
The type() function returns the data type of a variable.
47. What is type casting?
Type casting means converting one data type into another.
48. Difference between implicit and explicit type casting.
Implicit casting is done automatically by Python, while explicit casting is done by the programmer.
49. What is input() function?
The input() function takes input from the user.
50. What does input() return by default?
It returns data as a string.
51. Difference between print() and input().
print() displays output, while input() takes user input.
52. What are operators?
Operators are symbols that perform operations on values.
53. Types of operators in Python.
Arithmetic, relational, logical, assignment, bitwise, membership, and identity operators.
54. Difference between = and ==.
= assigns a value, == compares values.
55. Difference between is and ==.
is checks object identity, == checks value equality.
56. What are relational operators?
Operators that compare values, like <, >, <=, >=.
57. What are logical operators?
Operators like and, or, and not used to combine conditions.
58. What is short-circuiting in logical operators?
Evaluation stops as soon as the result is known.
59. What are bitwise operators?
Operators that work on bits, like &, |, and ^.
60. What is a conditional statement?
A statement that executes code based on a condition.
61. What is if statement?
It executes code when a condition is true.
62. What is elif?
elif checks another condition if the previous one is false.
63. What is else?
else executes code when all conditions are false.
64. Can if exist without else?
Yes, if can be used alone.
65. What is nested if?
An if statement inside another if.
66. What is a loop?
A loop repeats a block of code.
67. Why are loops used?
To avoid writing repetitive code.
68. What is a for loop?
A loop used to iterate over a sequence.
69. What is a while loop?
A loop that runs while a condition is true.
70. Difference between for and while loop.
for is sequence-based, while is condition-based.
71. What is infinite loop?
A loop that never stops.
72. What is break statement?
It exits the loop.
73. What is continue statement?
It skips the current iteration.
74. What is pass statement?
It does nothing and acts as a placeholder.
75. What is range() function?
It generates a sequence of numbers.
76. What does range(1, 10, 2) produce?
It produces odd numbers from 1 to 9.
77. Can range() be used in while loop?
No, it is mainly used with for loop.
78. What is loop else?
An else block after a loop.
79. When does loop else execute?
When the loop completes normally.
80. What is a function?
A function is a block of reusable code.
81. Why do we use functions?
To reduce repetition and improve readability.
82. How do you define a function?
Using the def keyword.
83. What is the syntax of a function?
def function_name(parameters):
84. What is function calling?
Executing a function using its name.
85. Difference between defining and calling a function.
Defining creates the function, calling executes it.
86. What are parameters?
Variables in function definition.
87. What are arguments?
Values passed to a function.
88. Difference between parameters and arguments.
Parameters receive values, arguments send values.
89. What is a return statement?
It sends a value back from a function.
90. Can a function return multiple values?
Yes, using tuples.
91. What happens if a function has no return?
It returns None.
92. What is default parameter?
A parameter with a predefined value.
93. How do default arguments work?
They are used if no value is passed.
94. What are positional arguments?
Arguments passed in order.
95. What are keyword arguments?
Arguments passed using parameter names.
*96. What is args?
It allows multiple positional arguments.
*97. Why is args used?
To pass variable number of arguments.
**98. What is kwargs?
It allows multiple keyword arguments.
**99. Why is kwargs used?
To handle named arguments dynamically.
**100. Can we use both *args and kwargs together?
Yes, in the same function.
101. What is variable scope?
It defines where a variable is accessible.
102. What is local scope?
Variables defined inside a function.
103. What is global scope?
Variables defined outside functions.
104. Difference between local and global variables.
Local variables are limited to functions, global variables are accessible everywhere.
105. What is the global keyword?
It allows modifying global variables inside a function.
106. Why do we need global keyword?
To change global variable values inside functions.
107. Can a function access a global variable?
Yes, for reading.
108. Can a function modify a global variable?
Yes, using global keyword.
109. What is nested function?
A function inside another function.
110. Can we define a function inside another function?
Yes.
111. What is function recursion?
A function calling itself.
112. What is base condition in recursion?
The condition that stops recursion.
113. What happens if base condition is missing?
It causes infinite recursion.
114. What is stack overflow?
It occurs when memory limit is exceeded due to recursion.
115. What is lambda function?
A small anonymous function.
116. Difference between lambda and normal function.
Lambda is single-expression and anonymous.
117. Can a function be assigned to a variable?
Yes.
118. What is a first-class function?
Functions treated like variables.
119. What is a higher-order function?
A function that takes or returns another function.'''
