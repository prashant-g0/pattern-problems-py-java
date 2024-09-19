# 1. pattern: Number of rows is equal to the number of columns 
            #for  n = 4     n = 3   n = 2
               #  ****      ***     **
               #  ****      ***     **
               #  ****      ***
               #  ****

#Code:

n = 4

for i in range(n):
    print("*" * n)


# 2. 
            #for  n = 4      
               #  ABCD    
               #  ABCD    
               #  ABCD   
               #  ABCD

#Code:

n = 4

for i in range(n):
    for j in range(n):
        print(chr(65+j), end="")
    print()


# 3. 
            #for  n = 4      
               #   1 2 3 4   
               #   5 6 7 8  
               #   9 10 11 12  
               #  13 14 15 16

#Code:

n = 4
num = 1

for i in range(n):
    for j in range(n):
        print(num," ", end="")
        num += 1
    print()


# 4. 
            #for  n = 4      
               #    A B C D     
               #    E F G H    
               #    I J K L      
               #    M N O P   

#Code:

n = 4
num = 65

for i in range(n):
    for j in range(n):
        print(chr(num)," ", end="")
        num += 1
    print()

