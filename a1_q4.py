low = int(input("enter lower limit of range:"))
high = int(input("enter upperr limit of range:"))
for x in range (low,high+1):
    for i in range (2,x):
        if x % i == 0:
            break
    else:
        print(x)
