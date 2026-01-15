#1. Write a Python program that takes a list of elements as input and removes duplicate elements, while preserving the original order. Do not use the set() data structure.

2#. Write a Python program that takes a list of integers and finds the second largest
#element by traversing the list only once.
'''li=list(map(int,input("enter list of numbers: ").split()))
first_largest=0
second_largest=0
for num in li:
    if num > first_largest:
        second_largest=first_largest
        first_largest=num
    elif second_largest < num and num < first_largest:
        second_largest=num 

print("second largest number is :", second_largest)           


#3. Write a Python program that takes a list and an integer k as input and rotates the
#list to the right by k positions.



# 4. Write a Python program that takes a list of integers and a target sum, and finds all
#pairs of elements whose sum equals the target value.
li=list(map(int,input("enter list of numbers: ").split()))
target_sum=int(input("enter target sum: "))

for i in li:
    for j in li:
        if i+j==target_sum:
            print(f'the target sum pair is: {i} and {j}')'''

#Write a Python program that checks whether a given list of numbers is already
#sorted in ascending order.
li=list(map(int,input("enter list of number: ").split()))
is_sorted=True
for i in range(len(li)-1):
    if li[i]> li[i+1]:
        is_sorted=False
        break
if is_sorted:
    print("the list is sorted") 
else:    
    print("the list is not sorted")   


#Write a Python program that checks whether a given list of numbers is already
#sorted in ascending order.