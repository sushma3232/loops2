

n=5
for i in range(n):
    a=1
    for j in range(i+1):
        print("  ",end="")
    for j in range(i,n):
        print(a,end=" ")
        a=a+1
    print()
    
    
i=5
while i>=1:
    k=0
    while k<=6-i-1:
        print("  ",end="")
        k=k+1
    j=5
    while j>5-i:
        print(6-j,end=" ")
        j=j-1
    print()
    i=i-1