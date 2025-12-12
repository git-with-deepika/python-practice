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
sentence= "capitalize the first letter of the word of the sentence or paragraph".upper()
print(sentence)