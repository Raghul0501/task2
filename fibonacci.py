n=int(input("Enter the length of Fibonacci seies:"))
a=0;b=1
print(f"{a},{b}",end=",")
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=",")

