#pattern: to print a hollow diamond shape
#       *    
#      * *   
#     *   *  
#    *     * 
#   *       *
#   *      * 
#    *    *  
#      * *   
#       *    



#Code:

n = 5  # The number of rows in the upper half of the diamond

# Print the upper half of the diamond
for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end=' ')
    
    # Print the first character of the current row
    print("*", end='')
    
    # Print the hollow part
    if i > 0:
        for j in range(2 * i - 1):
            print(" ", end=' ')
        # Print the last character of the current row if not the first row
        print("*", end='')
    
    # Move to the next line after each row
    print()

# Print the lower half of the diamond
for i in range(n - 2, -1, -1):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end=' ')
    
    # Print the first character of the current row
    print("*", end='')
    
    # Print the hollow part
    if i > 0:
        for j in range(2 * i - 1):
            print(" ", end=' ')
        # Print the last character of the current row if not the first row
        print("*", end='')
    
    # Move to the next line after each row
    print()
