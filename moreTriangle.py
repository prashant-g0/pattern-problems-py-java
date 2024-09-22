# 1. Reverse triangle pattern 
            #for  n = 4      
               #  1    
               #  2 1    
               #  3 2 1   
               #  4 3 2 1

#Code:

n = 4

for i in range(1,n+1):
    for j in range(0,i):
        print(i," ", end="")
        i -= 1
    print()


# 2. Floyd's triangle pattern  
            #for  n = 4      
               #  1   
               #  2 3    
               #  4 5 6   
               #  7 8 9 10

#Code:

n = 4
a = 1

for i in range(1,n+1):
    for j in range(0,i):
        print(a," ", end="")
        a += 1
    print()


# 3. Inverted triangle pattern  
            #for  n = 4      
               #  1 1 1 1    
               #    2 2 2    
               #      3 3   
               #        4

#Code:

n = 4

for i in range(n+1):
    for j in range(i):
        print(" ", end="")
    for j in range(n-i):
        print(i+1,end="")
    print()