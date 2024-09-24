#1. Butterfly pattern
        #for n = 5
            # *        *
            # **      **
            # ***    ***
            # ****  ****
            # **********
            # ****  ****
            # ***    ***
            # **      **
            # *        *

#Code:

n = 5
    
for i in range(1, n+1):
        # Left wing
    for j in range(1, i+1):
        print("*", end="")
        # Spaces in the middle
    for j in range(2*(n-i)):
        print(" ", end="")
        # Right wing
    for j in range(1, i+1):
        print("*", end="")
    print()

    # Lower half of the butterfly
for i in range(n, 0, -1):
        # Left wing
    for j in range(1, i+1):
        print("*", end="")
        # Spaces in the middle
    for j in range(2*(n-i)):
        print(" ", end="")
        # Right wing
    for j in range(1, i+1):
        print("*", end="")
    print()
