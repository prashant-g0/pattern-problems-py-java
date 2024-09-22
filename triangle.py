# 1. 
            #for  n = 4      
               #    *    
               #    * *      
               #    * * * 
               #    * * * *

#Code:

n = 4

for i in range(n):
    for j in range(i+1):
        print("*"," ", end="")
    print()


# 2. 
            #for  n = 4      
               #  1    
               #  2 2   
               #  3 3 3   
               #  4 4 4 4

#Code:

n = 4

for i in range(n+1):
    for j in range(i):
        print(i," ", end="")
    print()


# 3. 
            #for  n = 4      
               #  A    
               #  B B    
               #  C C C  
               #  D D D D

#Code:

n = 4
num = 65

for i in range(1,n+1):
    for j in range(i):
        print(chr(num)," ", end="")
    num += 1
    print()


# 4. 
            #for  n = 4      
               #  1    
               #  1 2     
               #  1 2 3    
               #  1 2 3 4

#Code:

n = 4

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j," ", end="")
    print()