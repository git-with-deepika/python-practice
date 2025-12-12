# basic question of string
a='hello world'
print(a[0:6])

n=input("enter string: ")
print(len(n))
print(n[1:len(n)-1])

n='pythonprogramming'
print(len(n))
print(n[0:6] )
print(n[6:len(n)])

a='apple'
print(a[::-1])



n='pythonprogramming'
print(len(n))
print(n[0:len(n):+2])

n='pythonprogramming'
print(len(n))
print(n[1:len(n):2])

n="LearningPython"
print(len(n))
print(n[-14:-6])
print(n[-6:])


st='python'
n=len(st)//2
print(st[0:n])
print(st[n:len(st)])

st='datascience'
print(st[4:len(st)])

n="PythonProgramming"
print(n[-11:-8])

n='this is sentence'
print(n[-8:-1])

st=input("enter string: ")
n=int(input("enter number: "))
print("first",n, "charactres", st[0:n])

n=input("enter string: " )
rev=n[::-1]
print(rev)
if rev==n:
    print("palindrone")
else:
    print("not palindrome")    

st="SlicingExamples"
print(st[0:len(st) :2])

st="SlicingExamples"
print(len(st))
print(st[3:12])

st="abcdefghijklmnop"
print(st[7:11])



st=input("enter string: ")
print(st[-4:])

st="OpenAIChatGPT"
print(st[0:7])
print(st[4:10])
print(st[::-1])

st=input("enter string")
print(st[1:len(st):2])

st="ABCDEFG"
print(st[0:len(st):2])

st="HelloPython"
print(st[3:7])

s=input("enter: ")
result=s+s
print(result[::2] + result[1::2])

st=input("enter: ")
for ch in st:
    print(ch*2)

# reverse a string without slicing
st=input("enter string: ")
reverse_st=""
for ch in st:
    reverse_st=ch+reverse_st

print(reverse_st)    