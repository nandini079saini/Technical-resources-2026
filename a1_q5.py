n = int(input("Enter the number : "))
num=0
d=0

while n>0:
    num=n%10
    n=n//10
    d+=1

print(d,"is the number of digits in",n)
