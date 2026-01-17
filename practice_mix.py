                   #  🔹LIST – Coding Questions (1–15)

#1. Write a Python program that takes a list of elements as input and removes duplicate elements, while preserving the original order. Do not use the set() data structure.
original_li=list(map(int,input("enter list of number: ").split()))
new_list=[]
for i in original_li:
    if i not in new_list:
        new_list.append(i)
print("original list is :",original_li)        
print("new list is :",new_list)        

2#. Write a Python program that takes a list of integers and finds the second largest
#element by traversing the list only once.
li=list(map(int,input("enter list of numbers: ").split()))
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
li=[1,2,3,4,5]
k=int(input("enter rotation number"))
k=k% len(li)
for i in range(k):
  element=li.pop()
  li.insert(0,element)
print(li)  



# 4. Write a Python program that takes a list of integers and a target sum, and finds all
#pairs of elements whose sum equals the target value.
i=list(map(int,input("enter list of numbers: ").split()))
target_sum=int(input("enter target sum: "))

for i in li:
    for j in li:
        if i+j==target_sum:
            print(f'the target sum pair is: {i} and {j}')

#5. Write a Python program that checks whether a given list of numbers is already
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


#6. Write a Python program that takes a nested list (which may contain lists inside lists
#at any depth) and flattens it into a single list.
li=[[1,2],[3,4],[5,6],[7,8]]
li1=[]
for i in li:
    for j in i:
        li1.append(j)

print(li1) 


#7. Write a Python program that moves all zero elements to the end of the list while
#maintaining the relative order of the non-zero elements.
li=[1,2,4,3,0,5,0,6,0,0,7]
li_zero=[]
li_non_zero=[]
for i in li:
    if i !=0:
        li_non_zero.append(i)
    else:
        li_zero.append(i)

print("the non zero list is:",li_non_zero)
print("the zero list is:",li_zero)           

#8. Write a Python program that counts the frequency of each element in a list and
#displays the result.
li=[1,2,1,3,2,4,5,6,7,6]
fre={}
for num in li:
    if num in fre:
        fre[num]+=1
    else:
        fre[num]=1 
print(f'the frequency is: {fre}')   

# 9. Write a Python program that finds the common elements between two lists,
#without using the set() data structure.
li1=[10,20,34,40,45,50]
li2=[10,22,34,41,50,55]
for i  in range(len(li1)):
    for j in range(len(li2)):
        if li1[i]==li2[j]:
            print(f'the common element between li1 and li2  is:{li1[i]}')

#10. Write a Python program that removes all elements located at even index positions
#from a list.
li=[11,12,32,45,55,67,90]
for i in range(len(li)-1,-1,-1):
    if i%2==0:
        li.pop(i)
print(li)   

 # 11. Write a Python program that splits a list into smaller sublists (chunks) of size n.              
li=list(map(int,input("enter list :").split()))
n=int(input("enter chunk size (n): "))
chunk=[]
for i in range(0,len(li),n):
    chunk=li[i:i+n]
    chunk.append(chunk)
print(chunk)    

#12. Write a Python program that merges two already sorted lists into a single sorted list. 
li=[1,2,4,3,6,5]
li1=[7,9,8,10,12,11]
merge_list=[]
li.sort()
li1.sort()
merge_list=li+li1
print("merge  list li and li1: ",merge_list)

# 13. Write a Python program that finds the missing number from a list containing
#numbers from 1 to n, with exactly one number missing.
li=list(map(int,input("enter list of number").split()))
n=len(li)+1 # because 1 number is missing
expected_sum= (n*(n+1))//2
actual_sum=0

for i in range(len(li)):
    actual_sum=actual_sum+li[i]

missing_number=expected_sum-actual_sum
print("actyal sum is: ",actual_sum)    
print("expected sum is: ",expected_sum)
print("the missing number is: ",missing_number)

               # 🔹 TUPLE – Coding Questions (16–25)

#16. Write a Python program that finds the maximum and minimum elements in a tuple
#of numbers.               
tup=(20,23,34,45,65,55)
max_element=tup[0]
min_element=tup[0]
for num in tup:
    if num > max_element:
        max_element=num
        
    if num < min_element :
        min_element=num 

print("maximum element in tuple is: ",max_element)
print("minimum element in tuple is: ",min_element)    

#17. Write a Python program that converts a tuple into a list, performs a modification,
# and then converts it back into a tuple.

tup=(22,34,34,43,54,56,65)
print(f'original tuple: {tup}')
li=list(tup)
print("after converting tuple into list the list is:  ",li)
li[3]=55
print(f'after modifying list: ',li)

tup=tuple(li)
print(f'converting back list into tuple: {tup} ') 

# 18. Write a Python program that counts the number of occurrences of a given element in a tuple.
tup=tuple(map(int,input("enter number of tuple: ").split()))
element=int(input("enter element: "))
count=0
for i in tup:
    if i==element:
        count+=1

print("the occurrence of element is : ",count)        

# 19. Write a Python program that removes duplicate elements from a tuple and returns a new tuple.
                                 # methoa 1
tup=tuple(map(int,input("enter number of tuple: ").split()))
new_tup=(set(tup))
new_tup=tuple(new_tup)
print(f'originl tuple: {tup}')
print(f'new tuple : {new_tup}') 
                                    # method 2
tup=tuple(map(int,input("enter number of tuple: ").split()))  
print(f'original tuple: {tup}')     
li=list(tup)
li1=[]
for i in li:
    if i not in li1:
        li1.append(i)      
print(f'list is: {li1} ')              
tup=tuple(li1)  
print(f'tuple after removing duplicate element: {tup}')          

#20.Write a Python program that sorts a tuple of integers and returns a new sorted tuple.
tup=tuple(map(int,input("enter number of tuple: ").split())) 
li=list(tup)
for i in range(len(li)):
    for j in range(0,len(li)-i-1):
        if li[j] > li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
new_tup=tuple(li)
print(f'tuple after sorting: {new_tup}')       

#21. Write a Python program that finds the index of a specific element in a tuple,
#without using the built-in index() method.
tup=tuple(map(int,input("enter number of tuple: ").split())) 
element=int(input("enter element: "))
found=False
for i in range(len(tup)):
    if tup[i]==element:
        
        found=True
        break
if found == True:
    print(f'the element is {element} an the index is {i}')
if   not found:
    print(f'element {element} not found ')        

#22.Write a Python program that unpacks a tuple into multiple variables and prints each variable.
tup=(23,34,34 ,56 ,76)
a,b,c,d,e=tup
print(a,b,c,d,e)

#23.Write a Python program that checks whether a tuple is a palindrome, meaning it reads the same forward and backward.
tup=(1,2,3,2,1)
is_palindrome=True
for i in range(len(tup)):
    if tup[i] != tup[len(tup)-i-1]:
        is_palindrome=False
        break
if is_palindrome:
    print("tuple is palindrome")
else:
    print("tuple is not palindrome ")        

# 24.Write a Python program that merges two tuples element-wise (pairing elements at the same index).
tup1=(1,2,3,4,5)
tup2=(6,7,8,9,10)
merge_tup=tuple(zip(tup1,tup2))
print(f'merge tuple is : {merge_tup}')

# 25. Write a Python program that finds the common elements between two tuples.
tup1=(1,2,3,4,5)
tup2=(1,4,6,3,7)
for i in range(len(tup1)):
    for j in range(len(tup2)):
        if tup1[i]==tup2[j]:
            print(f'the comman element between both tuple is: {tup1[i]}')

                           # 🔹 SET - Coding Questions (26-35)
#26.Write a Python program that removes duplicate elements from a list using a set
#and converts the result back into a list.
li=[1,2,2,3,4,2,3,5,6,7]
print(f'list before sorting: {li}')
tu=set(li)
li=list(tu)
print(f'list after sorting: {li}') 


# 27. Write a Python program that finds the union, intersection, and difference of two sets.
se={1,2,3,4,5,6,7}
se2={1,2,4,8,9,10,11}
print(f'union of both set: {se|se2}')
print(f'intersection of both set: {se & se2}')
print(f'difference of both set: {se-se2}') 

#28.Write a Python program that checks whether one set is a subset of another set.
setA={1,2,3}
setB={1,2,3,4,5}
is_subset=True
for i in setA:
    if i not in setB:
        is_subset=False
        break
if is_subset:
    print("setA is subset of setB")
else:
    print("not subset")        

#29.Write a Python program that finds the elements present in the first set but not in the second set.
setA={1,2,3}
setB={4,5,6}
is_present=True
for element in setA:
    if element not in setB:
        is_present=False
        break
if is_present:
    print("the element in setA present in setB")
else:
    print("the element in setA not present in setB") 

# 30.Write a Python program that removes the common elements from two sets, leaving only unique elements in each.
setA={1,2,3,4,5}
setB={4,5,6,7}
uniqueA=setA.difference(setB)
uniqueB=setB.difference(setA)
print(uniqueA)
print(uniqueB) 

#31. Write a Python program that finds the symmetric difference between two sets.
setA={1,2,3,4,5}
setB={4,5,6,7}
unique=setA ^ setB
unique1=setA.symmetric_difference(setB)
print(unique)
print(unique1) 

# 32.Write a Python program that checks whether two sets are disjoint, meaning they have no elements in common.
se={1,2,3}
se2={4,5,6}
is_disjoint=True
for element in se:
    if element in se2:
        is_disjoint=False
        break
if is_disjoint:
    print(" disjoint set")
else:
    print(" Not disjoint set")        

#33.Write a Python program that converts a list of lists into a set of tuples so that duplicates can be removed.
list_of_list=[[1,2],[3,4],[1,2]]
unique_set=set()
for inner_list in list_of_list:
    t=tuple(inner_list)
    unique_set.add(t)
print(unique_set)    



#34.Write a Python program that counts the number of unique vowels present in a string using a set.
str='hey i am deepika'
s=set(str)
vowel='aeiouAEIOU'
unique_set=set()
for char in s:
    if char in vowel:
        unique_set.add(char)
print(unique_set)
count=len(unique_set)     
print(count)   


#35. Write a Python program that removes duplicate characters from a string using a set, while preserving the original order.
str='programming in python'
# Create an empty set to track seen characters
str2=set()
# Create a list to store result characters in order
result=[]

for ch in str:
    if ch not in str2:
        str2.add(ch)
        result.append(ch)
# Join the list back into a string
final_result=''.join(result)
print(final_result)  


                          # 🔹 STRING – Coding Questions (36–50)      

# 36.Write a Python program that reverses a string without using slicing.
str='hello'
rev=''
for ch in str:
    rev=ch+rev
print(rev) 

# 37. Write a Python program that checks whether a given string is a palindrome.
str="hello"
rev=''
x=str
for ch in str:
    rev=ch+rev
if rev==x:
    print("palindrome") 
else:
    print("not palindrome")     

# 38.Write a Python program that checks whether two strings are anagrams of each other.
str1='abc'
str2='bca'
is_anagram=True
for ch in str1:
    if ch not in str2:
        is_anagram=False
        break
if is_anagram:
    print("anagram ") 
else:
    print("not anagram")         

# 39.Write a Python program that finds the first non-repeating character in a string.
str='hello this is deepika'
non_repeat=''
for ch in str:
    if ch not in non_repeat:
        non_repeat+=ch
print("non_repeating character:",non_repeat)    

#40.Write a Python program that counts the frequency of each character in a string.
str='deepika'
dic={}
for ch in str:
    
    if ch  in dic:
        dic[ch]+=1
    else:
        dic[ch]=1 
print(dic)          

# 41. Write a Python program that removes all special characters from a string, keeping only alphabets and digits.
s='hello! $ my name deepika#'
result=''
for ch in s:
    if ch.isalnum():
        result+=ch
print(result)   

# 42.Write a Python program that finds the longest word in a given sentence.
s='hello this is deepika'
word=s.split()
longest=word[0]
for ch in word:
    if len(ch) > len(longest):
        longest=ch
print(longest)        

# 43.Write a Python program that capitalizes the first letter of each word in a sentence.
s='hello this is deepika'
word=s.split()
result=''
for ch in word:
     result+=ch.capitalize()
print(result)   

# 44.Write a Python program that checks whether a string contains only digits.
s='hello123'
if s.isdigit():
    print("string contains only digits")
else:
    print("string also contain character")    

# 45.Write a Python program that replaces all vowels in a string with the * character.
s='my name is deepika'
vowel='aeiouAEIOU'
result=''
for ch in s:
    if ch in vowel:
        result+="*"
    else:
        result+=ch
print(result)            

# 46.Write a Python program that counts the number of words in a sentence.
sent='hello python'
count=0
for ch in sent:
    count+=1
print(count)    

# 47. Write a Python program that finds duplicate characters in a string.
s='hello python'
duplicate={}
for ch in s:
    if ch in duplicate:
        duplicate[ch]+=1
    else:
        duplicate[ch]=1
print(duplicate)            
for ch in duplicate:
    if duplicate[ch] >= 2:
        print(f'duplicate character: {ch}-> {duplicate[ch]}') 

# 48.Write a Python program that removes consecutive duplicate characters from a string.
st='aaabbbccc'
word=str[0]
for ch in range(1,len(st)):
    if st[ch] != st[ch-1]:
        word+=st[ch]
print(word)        

# 49.Write a Python program that checks whether a sentence is a valid palindrome, ignoring spaces, punctuation, and case.


# 50.Write a Python program that finds the most frequently occurring character in a string.
text='success'
count={}
for char in text:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print(count)            
max_char=''
max_count=0
for char in count:
   if max_count < count[char]:
    max_count=count[char]
    max_char=char
print(f'frequency character is :{max_char} and frequency is :{max_count}')


                    # 🔹 DICTIONARY – Coding Questions (51–60)

# 51. Write a Python program that counts the frequency of each element in a list using a dictionary.
li=[1,1,2,3,3,4,5,6]
fre={}
for num in li:
    if num in fre:
        fre[num]+=1
    else:
        fre[num]=1
print(fre)           

# 52.Write a Python program that counts the frequency of each word in a sentence using a dictionary.
sent='hello'
fre={}
for ch in sent:
    if ch in fre:
        fre[ch]+=1
    else:
        fre[ch]=1 
print(fre)        

# 53.Write a Python program that sorts a dictionary by its values in ascending or descending order.


#54.Write a Python program that finds the key associated with the maximum value in a dictionary.
my_dict = {'apple': 10, 'banana': 25, 'cherry': 15, 'date': 5}
max_value=0
max_key=''
for key ,value in my_dict.items():
    if max_value<value:
        max_value=value
        max_key=key
print(f'max_key is :{max_key} and max_value is :{max_value}')        


# 55. Write a Python program that merges two dictionaries into a single dictionary.
dic1={'a':1,'b':2}
dic2={'c':3,'d':4}
dic1.update(dic2)
print(dic1)    

# 56. Write a Python program that removes dictionary entries that have duplicate values, keeping only one unique value.
data={'a':10,'b':20,'c':10,'d':30,'e':20}
result={}
for key,value in data.items():
    if value not in result.value:
        result[key]=value
print('cleande: ',result)        

# 57. Write a Python program that inverts a dictionary, meaning keys become values and values become keys.
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}
print("original dictionary: ",my_dict)
inverted_dict={}
for key,value in my_dict.items():
    inverted_dict[value]=key
print("new inverted dictionary: ",inverted_dict)    

# 58.Write a Python program that checks whether two dictionaries are equal, regardless of key order.
dict1 = {'apple': 10, 'banana': 20, 'cherry': 30}
dict2 = {'cherry': 30, 'banana': 20, 'apple': 10}
print("dict1: ",dict1)
print("dict2: ",dict2)
if dict1==dict2:
    print("both dictionariea are equal")
else:  
    print("both dictionariea  not are equal")  



#59.Write a Python program that groups dictionary keys that have the same value together.
my_dict = {'apple': 1, 'banana': 2, 'cherry': 1, 'date': 2, 'fig': 3}
print("original dictionary: ",my_dict)
new_dict={}
for key,value in my_dict.items():
    if value in new_dict:
        new_dict[value].append(key)
    else:
        new_dict[value]=[key] 
print('new dictionary: ',new_dict)           
#60.Write a Python program that finds the first non-repeating character in a string using a dictionary.
text = "success"
count={}
for char in text:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print(count)            
non_repeating={}
for char in text:
    if count[char]==1:
        non_repeating[char]=count[char]
        
print(non_repeating)    