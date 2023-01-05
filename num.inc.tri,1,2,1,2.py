

n=5
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print("1",end=" ")
        else:
            print("2",end=" ")  ,
    print()
    
    
i=1
while i<=5:
    j=1
    while j<=i:
        if i%2!=0:
            print("1",end=" ")
        else:
            print("2",end=" ")
        j=j+1
    print()
    i=i+1