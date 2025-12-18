# string concatintion
first_name=input("enter first_name: ")
last_name=input("enter last_name: ")
age=input("enter your age: ")
full_name=first_name+" "+last_name
print("full_name: ",full_name)

sentence="hello this is my name: "+full_name+" and this is my age: "+age
print(sentence)
 # formated string
print(f'hello this is my name {full_name} and this is my age {age}')

# .title():-> for first word capital
first_name=input("enter first_name: ") .title()
last_name=input("enter last_name: ") .title()
age=input("enter your age: ")
full_name=first_name+" "+last_name
print("full_name: ",full_name)
print(f'hello this is my name {full_name} and this is my age {age}')

# capitalize():-> capitalize the first letter of the word of the sentence or paragraph
sentence= "capitalize the first letter of the word of the sentence or paragraph".capitalize()
print(sentence)

# upper():-> convert all the letter into uppercase
first_name=input("enter first_name: ").upper()
last_name=input("enter last_name: ").upper()
age=input("enter your age: ")
full_name=first_name+" "+last_name
print("full_name: ",full_name)
sentence= "capitalize all letter of the word of the sentence or paragraph".upper()
print(sentence)

# lower():-> convert all letter into lower
first_name=input("enter first_name: ").lower()
last_name=input("enter last_name: ").lower()
age=input("enter your age: ")
full_name=first_name+" "+last_name
print("full_name: ",full_name)
sentence= "Convert All LETTER of the word of the sentence or paragraph into lower".lower()
print(sentence)

# .isalpha():-> to check a string is alphabetic or not
first_name=input("enter first_name: ").isalpha()
last_name=input("enter last_name: ").isalpha()
sentence= "Convert All LETTER of the word of the sentence or paragraph into lower".isalpha()
print(sentence)# it will here give us false because of spaces in the sentene

#.isnumeric()
age='21'
print(age.isnumeric())
name='deepika'
print(name.isnumeric())

#alnum: to check alpha and numeric
age='21asd'
print(age.isalnum())
name='deepika'
print(name.isalnum())

#.split():-> to break word on the bases on spaces or given condtion(-,:)
sentence= "capitalize all letter of the word of the sentence or paragraph".split()
print(sentence)

# strip ,lstrip, rstrip: remove leading and trailing spaces from a string
name=" this is my name"
name.lstrip()
print(name)

name="this is my name    "
name.rstrip()
print(name)

# replace
st='this is string'
result=st.replace(" ","_")
print(result)

# length of string without using len()
st='this is string'
count=0
for ch in st:
    count+=1
print(count)

# number of digit
st=input("enter no: ")
count=0
for ch in st:
    if ch.isnumeric():
        count+=1
print(count)



