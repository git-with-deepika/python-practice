#****
# ****
#   ****
#     ****
num=4
for i in range(num):
    for j in range(i):
        print(" ",end=" ")
    for k in range(num):
        print("*",end=' ')
    print()        



#*******
#*     *
#*     *
#*     *
#*******
row=5
col=7

for i in range(1,row+1):
    for j in range(1,col+1):
        if i==1 or j==1 or i==row or j==col:
            print("*",end="")
        else:
            print(' ',end="")
    print()
#A 
#A B
#A B C
#A B C D
#A B C D E
a=65
for i in range(1,6):
    for j in range(i):
        print(chr(a+j),end=' ')   
    print()   

#A 
#B B
#C C C
#D D D D
#E E E E E
a=65
for i in range(1,6):
    for j in range(i):
        print(chr(a),end=' ')   
    print()
    a+=1 

#E ######################
#E F
#E F G
#E F G H
#E F G H I
#        * 
#      * *
#    * * *
#  * * * *
#* * * * *
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=' ')
    print()

#        1 
#      1 2
#    1 2 3
#  1 2 3 4
#1 2 3 4 5
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=' ')
    print()         
#1 2 3 4 5 
#  1 2 3 4
#    1 2 3
#      1 2
#        1

n=6
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=' ')
    print()  
#A B C D E 
#  A B C D
#    A B C
#      A B
#        A
n=5
a=64
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(1,i+1):
        print(chr(a+k),end=' ')
    print()   

#        * * * * * 
#      * * * * *
#    * * * * *
#  * * * * *
#* * * * *

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,n+1):
        print("*",end=' ')
    print()         
#        1 2 3 4 5 
#      1 2 3 4 5
#    1 2 3 4 5
#   1 2 3 4 5
#1 2 3 4 5
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,n+1):
        print(k,end=' ')
    print()        
#        A B C D E 
#      A B C D E 
#    A B C D E 
#  A B C D E 
#A B C D E 
n=5
a=64
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,n+1):
        print(chr(a+k),end=' ')
    print()
#    *
#   ***
#  *****
# *******
#*********
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    for k in range(1,i+1):
        print("*",end='')
    for k in range(2,i+1):
        print("*",end='')
    print()  

#     *
#    * *
#   *   *
#  *     *
# *********
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    for k in range(1,i+1):
        if i==n or k==1 or k==n :
         print("*",end='') 
        else:
         print(" ",end='')   
    for k in range(2,i+1):
        if i==n or k==1 or k==n or k==i:
         print("*",end='') 
        else:
         print(" ",end='')   
    print()    
# *******
#  *****
#   ***
#    *
n=4
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end='')
    for k in range(1,i+1):
        print("*",end='')
    for k in range(2,i+1):
        print("*",end='')
    print()    
#* 
#* * 
#* * * 
#* * * *
#* * * * *
#* * * *
# * * *
#* *
#*
n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=' ')
    print()    
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=' ')
    print()    
#        * 
#      * * 
#    * * * 
#  * * * * 
#* * * * * 
#  * * * * 
#    * * * 
#      * * 
#        * 
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=' ')   
    print()    
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=' ')   
    print()  

#        * 
#      * * * 
#    * * * * * 
#  * * * * * * * 
#* * * * * * * * * 
#  * * * * * * * 
#    * * * * * 
#      * * * 
#        *       
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    for k in range(2,i+1):
        print("*",end=' ')
    print()   
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    for k in range(2,i+1):
        print("*",end=' ')
    print()             

#1 
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()  
#1 2 3 4 5 
#1 2 3 4 
#1 2 3
#1 2
#1
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
#1 
#1 2 
#1   3 
#1     4 
#1 2 3 4 5 
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==n or j==1 or j==i:
         print(j,end=' ')
        else:
         print(' ',end=' ')
    print()  

#        1 #########
#      2 3 2
#    3 4 5 4 3
#  4 5 6 7 6 5 4
#5 6 7 8 9 8 7 6 5
n=5
temp=1
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=' ')
    a=i
    for k in range(i):
        print(a+k,end=' ')
    b=a+i-1
    for k in range(i-1):
        print(b-(k+1),end=' ')
        
    print()     


#        1 
#      1   2
#    1       3
#  1           4
#1 2 3 4 5 2 3 4 5
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        if  i==n or k==1:
         print(k,end=' ')
        else:
         print(" ",end=' ')
    for k in range(2,i+1):
        if k==i   or i==n:
         print(k,end=' ')
        else: 
         print(" ",end=' ')
    print()        
    
#1 2 3 4 5 
#1     4
#1   3
#1 2
#1
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
         print(j,end=' ')
        else:
           print(" ",end=' ') 
    print()    

#        * 
#      * * * 
#    * * * * * 
#  * * * * * * * 
#* * * * * * * * * 
#  * * * * * * * 
#    * * * * * 
#      * * * 
#        *      

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    for k in range(2,i+1):
        print("*",end=' ')
    print()   
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    for k in range(2,i+1):
        print("*",end=' ')
    print()      

#        1 
#      1 2 3
#    1 2 3 4 5
#  1 2 3 4 5 6 7
#1 2 3 4 5 6 7 8 9
#  1 2 3 4 5 6 7
#    1 2 3 4 5
#      1 2 3
#        1

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    a=i 
    for k in range(1,i+1):
        print(k,end=' ')
    for k in range(2,i+1):
        print((a+k)-1,end=' ')
    print() 
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(' ',end=' ')
    b=i+1
    for k in range(1,i+1):
        print(k,end=' ')
    for k in range(1,i):
        print((b+k)-1,end=' ')
    print()             


#1 2 3 4 5 6 7 8 9 
#  1 2 3 4 5 6 7 
#    1 2 3 4 5 
#      1 2 3 
#        1 
#     1 2 3 
#    1 2 3 4 5 
#  1 2 3 4 5 6 7 
#1 2 3 4 5 6 7 8 9 
n=5 
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end=' ')
    a=i  
    for k in range(1,i+1):
        print(k,end=' ')
    a=i-1     
    for k in range(2,i+1):
        print((a+k),end=' ')    
    print()    
for i in range(2,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    a=i  
    for k in range(1,i+1):
        print(k,end=' ')
    a=i-1     
    for k in range(2,i+1):
        print((a+k),end=' ')    
    print()    


###############

#A B C D E F G H I 
#  A B C D F G H
#    A B C F G
#      A B F
#        A
#      A B F
#    A B C F G
#  A B C D F G H
#A B C D E F G H I
n=5
d=68
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end=' ')
    a=i  
    for k in range(1,i+1):
        print(chr(64+k),end=' ')
    a=i-1    
    for k in range(2,i+1):
        print(chr(d+k),end=' ')    
    print()    
for i in range(2,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    a=i  
    for k in range(1,i+1):
        print(chr(64+k),end=' ')
    a=i 
    for k in range(2,i+1):
        print(chr(d+k),end=' ')    
    print()   
##############################
#* * * * * 
#*       *
#*       *
#*       *
#* * * * *
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==n or j==n or i==1:
         print("*",end=' ')
        else:
         print(' ',end=' ') 
    print() 
#1 2 3 4 5
#1       5
#1       5
#1       5
#1 2 3 4 5
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==n or j==n or i==1:
         print(j,end=' ')
        else:
         print(' ',end=' ') 
    print()        
#A B C D E
#A       E
#A       E
#A       E
#A B C D E
n=5
a=64
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==n or j==n or i==1:
         print(chr(a+j),end=' ')
        else:
         print(' ',end=' ') 
    print()               
#        * 
#      *   *
#    *       *
#  *           *
#*               *
#  *           *
#    *       *
#      *   *
#        *

n=5 
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        if   k==1  :
         print("*",end=' ')
        else:
           print(' ',end=' ') 
    for k in range(2,i+1):
            if  k==1 or k==i :
             print("*",end=' ')
            else:
             print(' ',end=' ') 
    print()        
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        if i==n or k==1  :
         print("*",end=' ')
        else:
           print(' ',end=' ') 
    for k in range(2,i+1):
            if i==n or k==1 or k==i :
             print("*",end=' ')
            else:
             print(' ',end=' ') 
    print()        


#        1 
#      1   1
#    1       1
#  1           1
#1               1
#  1           1
#   1       1
#      1   1
#        1
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        if   k==1  :
         print(k,end=' ')
        else:
           print(' ',end=' ') 
    for k in range(i-1,0,-1):
            if  k==1 or k==i :
             print(k,end=' ')
            else:
             print(' ',end=' ') 
    print()        
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        if i==n or k==1  :
         print(k,end=' ')
        else:
           print(' ',end=' ') 
    for k in range(i-1,0,-1):
            if i==n or k==1 or k==i :
             print(k,end=' ')
            else:
             print(' ',end=' ') 
    print() 

#        A ####################
#      A   B
#    A       C
#  A           D
#A               E
#  A           D
#    A       C
#      A   B
#        A 

n=5
a=64
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        if   k==1  :
         print(chr(a+k),end=' ')
        else:
           print(' ',end=' ') 
    for k in range(2,i+1):
            if  k==i :
             print(chr(a+k),end=' ')
            else:
             print(' ',end=' ') 
    print()        
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        if i==n or k==1  :
         print(chr(a+k),end=' ')
        else:
           print(' ',end=' ') 
    for k in range(2,i+1):
            if   k==i :
             print(chr(a+k),end=' ')
            else:
             print(' ',end=' ') 
    print() 

#*                 * 
#* *             * * 
#* * *         * * * 
#* * * *     * * * * 
#* * * * * * * * * * 
#* * * *     * * * * 
#* * *         * * * 
#* *             * * 
#*                 *

n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=' ')
    for k in range(2*(n-i)):
        print(' ',end=' ')
    for l in range(i):
        print("*",end=' ')
    print()        
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=' ')
    for k in range(2*(n-i)):
        print(' ',end=' ')
    for l in range(i):
        print("*",end=' ')
    print()   
          
