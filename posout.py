n=int(input("Enter number of elements:"))
l=[]
for i in range(n):
    l.append(int(input(f"Enter element{i+1}:")))
print(f"Input:{l}")
for i in l:
    if i < 0:
        l.remove(i)
print(f"Output:{l}")


