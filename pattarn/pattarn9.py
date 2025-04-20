rows = int(input("Enter number of rows: "))


for i in range(rows):
    #print spaces
    for j in range(i):
        print(" ", end="")

    #print star
    for k in range(2*rows-(2*i+1)):
        print("*",end="")

    print()