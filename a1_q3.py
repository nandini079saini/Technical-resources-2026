n = int(input("enter the number you want to check:"))

for i in range (2,n):
    if n % i == 0:
        print("number is not prime")
        break

else:
    print("number is prime")
    
