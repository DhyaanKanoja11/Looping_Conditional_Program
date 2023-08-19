n=int(input("Enter Range:"))
h=input("Enter String Or Numeric:")

for i in range(n):
    for a in range(0,i):
        print(h,end=" ")
    if  i<=3:
        print("", end=",")
    elif  i>=3:
        print("", end=",")
    else:
            print("",end="  ")

