a="KEERTHI"
n=len(a)
for i in range(n):
    for j in range(i+1):
        print(a[j],"@",end=" ")
    print()