print("LIST QUESTIONS")
print("              ")
#Basic

#Q-1. Create a list of 10 integers and print only even numbers.
li=[1,2,3,4,5,6,7,8,9,10]
for i in li:
  if i%2==0:
    print(f"Q1even no are{i}")

#Q- 2. Find the sum and average of elements in a list.
li =[1,2,3,4,5,6,7]
sum=0
count=0
avg=0
for i in li:
  sum+=i
  count+=1
print(f"Q2sum of elements is {sum}")
print(f"Q2avg of element is{sum//count}")

#Q-3Find the largest and smallest element in a list without using max(), min()
li = [1,2,3,4,5,7,67,23]
largest = li[0]
smallest =li[0]
for i in range(len(li)):
  if largest<li[i]:
    largest=li[i]
print(f"Q3the largest element is{largest}")
for j in range(len(li)):
  if smallest>li[i]:
    smallest=li[i]
print(f"Q3the smallest element is{smallest}")

#Q-4Count how many times a given element appears in a list.
li = [10, 20, 30, 10, 10, 40]
target =10
count = 0

for num in li:
    if num == target:
        count += 1
print(f"Q4-element is {count} time appears in list")

#Q-5Reverse a list using a for loop.
li = [1, 2, 3, 4, 5, 6, 7,8,9]
left = 0
right = len(li) - 1
while left < right:
    li[left], li[right] = li[right], li[left]
    left += 1
    right -= 1

print(f"Q5reverse list is{li}")

#Q-6Remove duplicate elements from a list.
li=[1,2,3,4,5,5,6,7,8,8,8]
unique_li=[]
for num in li:
  if num not in unique_li:
    unique_li.append(num)
print(f"Q6unique list are{unique_li}")

#Q-7 Merge two lists into a single list.
l1=[1,6,8,4]
l2=[4,6,5,3]
merge_li=[l1+l2]
print(merge_li)

#8. Sort a list in ascending order without using sort().
li = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(li)):
    for j in range(0, len(li) - i - 1):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print(f"Q8Sorted list is {li}")

#Intermediate

#9. Move all zeroes to the end of a list.
li = [0, 1, 0, 3, 12, 0, 8]
pos = 0
for i in range(len(li)):
    if li[i] != 0:
        li[pos], li[i] = li[i], li[pos]
        pos += 1
print(f"moved all zeros{li}")

#Q 10. Find the second largest element in a list.
li = [10, 20, 4, 45, 99, 99, 45]
first = 0
second= 0
for num in li:
    if num > first:
        second = first
        first = num
    elif num > second:
        second = num
print(f"Q10 first largest is {first}")
print(f"Q10 first largest is {second}")

#Q-11 Rotate a list to the right by 1 position.
li = [10, 20, 30, 40]
last_element = li.pop()
li.insert(0, last_element)

print(f"Q-11{li}")

#Q-12 Check if a list is a palindrome.
li = [1, 2, 3, 2, 1]
is_palindrome = True
left = 0
right = len(li) - 1
while left < right:
    if li[left] != li[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
print(f"Is Palindrome:{is_palindrome}")

#Q-13 Split a list into two halves.
li = [1, 2, 3, 4, 5, 6]
mid = len(li) // 2
first_half = li[:mid]
second_half = li[mid:]

print("First Half:", first_half)
print("Second Half:", second_half)

#Q-14 Find common elements between two lists.
l1=[1,2,3,4,5]
l2=[1,2,5,7,8]
for i in li:
  if i in l2:
    print(f"Q14 comman elements are-{i}")

#Q-15 Replace all negative numbers in a list with 0
l1=[-1,-2,7,4,-9,4]
for i in range(len(l1)):
  if l1[i]<0:
    l1[i]=0
print(l1)

print("              ")
print("TUPLE QUESTIONS")
print("              ")

#Basic
#Q-1. Create a tuple of numbers and print its length.
var=(1,2,3,4,5,6)
length = len(var)
print(f"Q1the length of list{var} is {length}")

#Q-2 Access the last element of a tuple.
my_tuple = ("Python", "Java", "C++", "JavaScript")
last_element = my_tuple[-1]
print("Q2The last element is:", last_element)

#Q-3 Convert a tuple into a list.
my_tuple = (10, 20, 30, 40)
my_list = list(my_tuple)
print("Q3Original Tuple:", my_tuple)
print("Q3New List:", my_list)

#Q-4 Count occurrences of an element in a tuple.
my_tuple = (1, 2, 3, 2, 4, 2, 5)
count_of_two = my_tuple.count(2)
print(f"Q4The number 2 appears {count_of_two} times.")

#Q-5 Find the maximum and minimum value in a tuple.
my_tuple = (45, 12, 89, 3, 56, 102, 7)
max_val = max(my_tuple)
min_val = min(my_tuple)
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")


#Intermediate
#6. Check if an element exists in a tuple.
fruits = ("apple", "banana", "cherry", "orange")
if "banana" in fruits:
    print("Q6Yes, 'banana' is in the tuple!")
else:
    print("No, it is not there.")

#Q7 Unpack a tuple into individual variables.
person = ("Alice", 25, "Engineer")
name, age, profession = person
print("Q7Name:", name)
print("Q7Age:", age)
print("Q7Profession:", profession)

#Q8 Convert a list of tuples into a dictionary.
list_of_tuples = [("id", 101), ("name", "Alice"), ("role", "Admin")]
result_dict = dict(list_of_tuples)
print(f"Q8change into dictionary{result_dict}")

#Q9 Find the index of an element in a tuple.
colors = ("red", "green", "blue", "yellow", "green")
idx = colors.index("blue")
print(f"The index of 'blue' is: {idx}")

#Q10 Reverse a tuple.
my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = my_tuple[::-1]
print(f"Q10-{reversed_tuple}")

print("              ")
#For loop question
print("              ")
#Q 1. Print numbers from 1 to 20
for i in range(1, 21):
    print("i", end=" ")

#Q 2. Print even numbers between 1 and 50
for i in range(2, 51, 2):
    print(i, end=" ")

#Q 3. Multiplication table of a given number
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
print()

#Q 4. Factorial of a number
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")
print()

# Q5. Sum of first n natural numbers
limit = 10
total = 0
for i in range(1, limit + 1):
    total += i
print(f"Sum of first {limit} numbers is {total}")


#Intermediate
# # 6. Count the number of digits in a number
num_digits = 12345
count = 0
for i in str(num_digits):
    count += 1
print(f"Number of digits in {num_digits}: {count}")

# 7. Print Fibonacci series up to n terms
n_terms = 8
a, b = 0, 1
print("Fibonacci series:", end=" ")
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b
print()

# 8. Check whether a number is prime
num_prime = 29
is_prime = True
if num_prime < 2:
    is_prime = False
else:
    for i in range(2, int(num_prime**0.5) + 1):
        if num_prime % i == 0:
            is_prime = False
            break
print(f"Is {num_prime} prime?: {is_prime}")

# 9. Print the pattern
print("Pattern:")
for i in range(1, 4):
    print("*" * i)

# 10. Find the sum of digits of a number
num_sum = 543
total_sum = 0
for digit in str(num_sum):
    total_sum += int(digit)
print(f"Sum of digits of {num_sum}: {total_sum}")

print("              ")
#STRING QUESTIONS
print("              ")
#Basic
# 1. Count the number of characters in a string
text1 = "Hello Python"
count = 0
for char in text1:
    count += 1
print(f"Total characters: {count}")

# 2. Count vowels and consonants
text2 = "Programming"
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0
for char in text2:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1
print(f"Vowels: {v_count}, Consonants: {c_count}")

# 3. Reverse a string using a loop
text3 = "Python"
reversed_text = ""
for char in text3:
    reversed_text = char + reversed_text
print(f"Reversed: {reversed_text}")

# 4. Check if a string is a palindrome
text = "radar"
if text == text[::-1]:
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is not a palindrome.")

# 5. Convert to uppercase without upper() (Using ASCII values)
text5 = "hello world"
upper_text = ""
for char in text5:
    if 'a' <= char <= 'z':
        upper_text += chr(ord(char) - 32)
    else:
        upper_text += char
print(f"Uppercase: {upper_text}")

#Intermediate
# 6. Count the frequency of each character
text6 = "banana"
freq = {}
for char in text6:
    freq[char] = freq.get(char, 0) + 1
print(f"Frequencies: {freq}")

# 7. Remove spaces from a string
text7 = "P y t h o n   i s   f u n"
no_spaces = ""
for char in text7:
    if char != " ":
        no_spaces += char
print(f"Without spaces: {no_spaces}")

# 8. Replace all vowels in a string with '*'
text8 = "Intelligence"
vowels = "aeiouAEIOU"
result8 = ""
for char in text8:
    if char in vowels:
        result8 += "*"
    else:
        result8 += char
print(f"Vowels replaced: {result8}")

# 9. Find the longest word in a sentence
sentence = "Coding in Python is amazing"
words = sentence.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print(f"Longest word: {longest}")

# 10. Check whether two strings are anagrams
str1 = "listen"
str2 = "silent"
is_anagram = sorted(str1) == sorted(str2)
print(f"Are '{str1}' and '{str2}' anagrams?: {is_anagram}")


#Combined logic
print("       ")

# 1. Given a list of strings, find the string with maximum length
words_list = ["apple", "banana", "cherry", "watermelon", "kiwi"]
max_str = words_list[0]
for s in words_list:
    if len(s) > len(max_str):
        max_str = s
print(f"String with max length: {max_str}")

# 2. Count how many times each word appears in a sentence
sentence = "Apple banana apple orange banana apple"
words = sentence.split()
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)

# 3. Find all palindromic strings from a list
my_list = ["radar", "hello", "level", "world", "madam"]
palindromes = []
for word in my_list:
    if word == word[::-1]:
        palindromes.append(word)
print(f"Palindromes: {palindromes}")

# 4. Convert a string into a list of words
text_string = "Learning Python is very rewarding"
list_of_words = text_string.split()
print(f"List of words: {list_of_words}")

# 5. From a tuple of numbers, create a list of only odd numbers
numbers_tuple = (1, 2, 3, 4, 5, 6)
odd_numbers = []
for x in numbers_tuple:
    if x % 2 != 0:
        odd_numbers.append(x)
print(odd_numbers)

