# 1. Use map to double each number in [1, 2, 3, 4, 5].
li=[1,2,3,4,5]
new=[]
def square(n):
    return n*n

mapped=list(map(square,li))
print(mapped)
   
# 2. Use map to convert ["10", "20", "30"] into integers.
num=['10','20','30']
converted=list(map(int,num))
print(converted)   

# 3. Use map with lambda to find the cube of each number in [2, 3, 4].
li=[2,3,4]
cube=list(map(lambda x: x**3,li))
print(cube)  

# 4. Use map to add 10 to each element in [5, 15, 25].
li1=[5,15,25]
def add(n):
    return 10+n

new=list(map(add,li1))
print(new)  

# 5. Use map to convert ["a", "b", "c"] into uppercase letters.
new_li=["a", "b", "c"]
conv_li=list(map(str.upper,new_li))
print(conv_li)   

# 6. Use map with lambda to find the length of each word in ["data", "science","ai"].
li=["data", "science","ai"]
length=list(map(lambda x: len(x),li))
print(length)  

# 7. Use map to convert a list of prices [100, 200, 300] into discounted prices by reducing 10%.
lis=[100, 200, 300]
def discount(d):
    dis=d-((d*10)/100)
    return dis

new_dis=list(map(discount,lis))
print(new_dis)

# 8. Use map with lambda to append "!" to each string in ["hi", "hello"].
st_li=["hi", "hello"]
new_li=list(map(lambda x : x + '!',st_li))
print(new_li) 

# 9. Use map to convert [1, 2, 3, 4] into their string form.
st=[1, 2, 3, 4]
new=list(map(str,st))
print(new) 

# 10. Use map with lambda to subtract 2 from each number in [10, 20, 30].
lis=[10, 20, 30]
new_list=list(map(lambda x : x-2,lis))
print(new_list)  

# 11. Use filter to extract only odd numbers from [1, 2, 3, 4, 5, 6].
fil=[1, 2, 3, 4, 5, 6]
fil2=list(filter(lambda x :  x%2 != 0,fil))
print(fil2)  

# 12. Use filter with lambda to get numbers greater than 25 from [10, 30, 20, 40].
filt=[10, 30, 20, 40]
print(list(filter(lambda x: x > 25,filt)))

#13. Use filter to keep only positive numbers from [-5, 3, -2, 7, 0].
positive=[-5, 3, -2, 7, 0]
print(list(filter(lambda x : x > 0 , positive)))

# 15. Use filter to select words longer than 3 characters from ["hi", "data", "ai", "python"].
cha=["hi", "data", "ai", "python"]
print(list(filter(lambda x : len(x) > 3 ,cha)))

# 16. Use filter with lambda to keep only numbers divisible by 5 from [10, 12, 15, 18, 20].
new=[10, 12, 15, 18, 20]
print(list(filter(lambda x : x%5==0,new)))  

# 17. Use filter to select strings that start with 'p' from ["python", "java", "php", "c"].
new_li=["python", "java", "php", "c"]
print(list(filter(lambda x: x.startswith('p'),new_li))) 

# 18. Use filter with lambda to extract all even numbers from [11, 22, 33, 44, 55].
lis=[11, 22, 33, 44, 55]
print(list(filter(lambda x : x%2==0,lis))) 

# 19. Use filter to remove empty strings from ["hello", "", "world", ""].
empt=["hello", "", "world", ""]
print(list(filter(lambda x : x != "",empt)))  

# 20. Use filter with lambda to keep values less than 50 from [10, 60, 30, 80, 40].
new=[10, 60, 30, 80, 40]
print(list(filter(lambda x : x<50,new))) 

# 21. Write a lambda function to check whether a number is positive or negative.
n=int(input("enter n :"))
check=lambda n : 'positive' if n > 0 else 'negative'
print(check(n))
  

# 22. Write a lambda function to return "Pass" if marks ≥ 40, else "Fail".
m=int(input("enter marks: "))
marks=lambda m : 'pass' if m >=40 else 'fail' 
print(marks(m))   

# 23. Write a lambda function to find the square of a number.
n=int(input("enter n :"))
square=lambda n : n**2
print(square(n))  

# 24. Write a lambda function to return "Adult" if age ≥ 18, else "Minor".
age=int(input("enter age: "))
p=lambda age: 'Adult' if age >=18 else 'Monor'
print(p(age)) 

# 25. Write a lambda function to find the maximum of two numbers.
find=lambda a,b: a if a>b else b
print(find(6,5))  

# 26. Write a lambda function to return "Even" or "Odd".
ev=lambda x: 'even' if x%2==0 else 'odd'
print(ev(10))  

# 27. Use map with a lambda to convert [1, 2, 3, 4] into "Odd" or "Even" labels.
li=[1, 2, 3, 4]
new=list(map(lambda x : 'even' if x%2==0 else 'odd',li))
print(new)  

# 28. Use filter with a lambda to keep only "Even" numbers from [1, 2, 3, 4, 5, 6].
li=[1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x%2==0,li))) 

# 29. Use map with a lambda to add "Mr. " before each name in ["Ram", "Shyam"].
li=["Ram", "Shyam"]
new=list(map(lambda x: 'mr.'+x ,li))
print(new) 

# 30. Use filter with a lambda to select only strings containing the letter 'a' from["cat", "dog", "apple"].
li=["cat", "dog", "apple"]
print(list(filter(lambda x : 'a' in x,li ))) 

# 31. Use map with a lambda to multiply each number in [2, 4, 6] by 3.
li=[2,3,6]
def multi(n):
    return n*3

mapped=list(map(multi,li))
print(mapped)  

# 32. Use filter with a lambda to remove all negative numbers from [-3, -1, 0, 2, 5].
li=[-3, -1, 0, 2, 5]
result=list(filter(lambda x : x>=0,li))
print(result)  

# 33. Use map with a lambda to convert temperatures [0, 20, 30] into Fahrenheit.
li=[0, 20, 30]
def temp(t):
    f= (t*9/5)+32
    return f

result=list(map(temp,li))
print(result)

# 34. Use filter with a lambda to keep only words ending with 'n' from ["python", "java", "c", "go"].
li=["python", "java", "c", "go"]
print(list(filter (lambda x: x.endswith('n'),li)))  

# 35. Use map with a lambda to replace each number in [1, 2, 3] with its boolean value (True or False).
li=[1, 2, 3]
mapped_ob=list(map(lambda x: True if x%2==0 else False,li))
print(mapped_ob)
