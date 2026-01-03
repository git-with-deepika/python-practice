#Basic list question

#Q1 Create a list of 5 arbitrary numerical values and print on console.
li = [1,2,3,4,5]
print(li)

#Q2 display only the first and the last element.
li = [1,2,3,4,5,6]
print(li[0],li[-1])

#Q3 print total no. of elements in list without using the built-in len() fun..
li = [1,2,3,4,5,6,7]
count=0
for i in li:
  count+=1
print(count)  

#Q4 chnge list by add new element to end only using list index & assign append() 

original_list = [1, 2, 3]
new_element = 4
original_list[len(original_list):] = [new_element]
print(f"List after adding {new_element}: {original_list}")

#Q5 change the value of  element located at third index pos. with a given value.
li = [1,2,3,4,5]
new_li = li[3]=8
print(li)

#Q6 make script accept 5 diff input from user stores all sequentially in list.
li = list(map(int,input("enter a list").split()))
print(li)

#Q7 Iterate a given list using a for loop and print each element on a new line.
li = [1,2,4,5,6]
for i in li:
  print(i)

#Q8 given list of integers, write code to print only the numbers that are even.
li = [ 1,2,3,4,5,6,7]
for i in li:
  if i%2==0:
    print(i)

#Q9 givenlist and target number,cal., printtotal occurrences target number list.
random_num = [10, 20, 10, 30, 40, 20, 10, 50, 20, 10]
target = 10
occurrence_count = 0

for number in random_num:
    if number == target:
        occurrence_count += 1

print(f"The list: {random_num}")
print(f"The target number: {target}")
print(f"Total occurrences of {target}: {occurrence_count}")

#Q10 Cal., print sum of numerical elements in list without using sum() function.
# Solution 10
price_list = [1.50, 5.00, 10.25, 20.75, 0.50]
total_sum = 0

for price in price_list:
    total_sum += price

print(f"The list of prices: {price_list}")
print(f"The total sum (manual calculation): {total_sum}")


#Intermediate List Questions

#Q1 Identify,print larg. value presentin list of numbers without max() function.
li = [45, 12, 88, 5, 93, 31, 7]
largest = li[0]
for i in range(len(li)):
        if largest<li[i]:
            largest = li[i]
print(f"The list: {li}")
print(f"The largest element: {largest}")

#Q2 Identify,print smallest element present list of num. without min() function.
li = [23,45,77,12,3,9]
smallest = li[0]
for i in range(len(li)):
  if smallest > li[i]:
    smallest = li[i]
print(f"The list: {li}")
print(f"The smallest element: {smallest}")    

#Q3 Createlist elements ofthe original list inreverse dontuse reverse(),slicing.
li = [1,2,3,4,5,6]
left = 0
right =len(li)-1
while left< right:
  li[left],li[right]=li[right],li[left]
  left+=1
  right-=1
print(li)  

#Q4 Sort list numbers in ascending order using the logic Bubble Sort algorithm.
data = [64, 34, 25, 12, 22, 11, 90]
n = len(data)
for i in range(n - 1):
   
    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print(f"Sorted list using Bubble Sort: {data}") 

#Q5 Generate new lifrom an original where allduplicate haveremoved,without set()
original_list = [10, 20, 10, 30, 40, 20, 50, 30]
unique_list = []

for element in original_list:
    if element not in unique_list:
        unique_list.append(element)

print(f"Original list: {original_list}")
print(f"List with duplicates removed: {unique_list}")

#Q6 Write function that checks whether a specified element is in within list.


#Q7 Print the elements from a list thatlocated at index position whicheven num.
data = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for i in range(len(data)):
    if i % 2 == 0:
        print(f"Index {i}: {data[i]}")

#Q8 Print only elements from a list that located at an index position which odd.
data = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for i in range(len(data)):
    if i % 2 != 0:
        print(f"Index {i}: {data[i]}")

#Q9 list and separately count and printtotal num even num. total number odd num.
int_list = [1, 5, 8, 12, 17, 20, 22, 31, 40]
even_count = 0
odd_count = 0
for number in int_list:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"The list: {int_list}")
print(f"Total Even Numbers: {even_count}")
print(f"Total Odd Numbers: {odd_count}")
   
#Q10 list print second list where each element square of the element in o list.  
original_nums = [2, 3, 4, 5, 6]
squared_nums = []

for num in original_nums:
    squared_nums.append(num * num)

print(f"Original list: {original_nums}")
print(f"Squared list: {squared_nums}")

#Q11 Combine the elements of two lists single new list without the + or extend()
list_a = [10, 20, 30]
list_b = [40, 50, 60]
combined_list = []
for item in list_a:
    combined_list.append(item)
for item in list_b:
    combined_list.append(item)

print(f"List A: {list_a}, List B: {list_b}")
print(f"Combined list: {combined_list}")

#Q12 Modify list in place so that all numbers less than zero  are removed.
data_list = [10, -5, 20, -1, 0, 30, -7, 40]
i = 0
while i < len(data_list):
    if data_list[i] < 0:
        del data_list[i]
    else:
        i += 1

print(f"List after removing negative numbers: {data_list}")

#Q13 Determine and print the second largest numerical value  list without sort
#Q14 Cyclic Right Shift
#Q15 Check ascending order
