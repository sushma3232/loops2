# n=int(input("enter the num"))
# s=n
# while s<=10:
#     sum=0
#     while s>0:
#         r=s%10
#         sum=sum+(r**2)
#         s=s//10
#     s=sum
# if n==1:
#     print(n,"is a happy number")
# else:
#     print(n,"not a happy number")
    
    
    
    
def digSum( n):
    sum = 0
     
    while(n > 0 or sum > 9):
     
        if(n == 0):
            n = sum
            sum = 0
         
        sum += n % 10
        n //= 10
     
    return sum
n = 57
print (digSum(n))




    
    
    
