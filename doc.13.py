n=int(input("enter the num"))
even_sum=0
odd_sum=0
i=1
while i<=n:
    if i%2==0:
        even_sum=even_sum+i**2
    else:
        odd_sum=odd_sum+i**2
    i=i+1
print(1+even_sum-odd_sum)