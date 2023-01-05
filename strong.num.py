n=int(input('enter the num'))
sum=0
a=n
while a>0:
    i=1
    fact=1
    r=a%10
    while i<=r:
	    fact=fact*i
	    i=i+1
    print("\n factorial of %d=%d"%(r,fact))
    sum=sum+fact
    n=n//10
print("\n sum of factorial of a given %d=%d(n,sum")
if sum==a:
	print("strong")
else:
	print("not strong")