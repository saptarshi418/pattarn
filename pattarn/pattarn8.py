rows = int(input("Enter number of rows: "))

for i in range(rows):
    # Print spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")
    
    for m in range(rows - i - 1):
        print(" ", end="")
    print()
