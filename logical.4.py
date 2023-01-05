# PRINT THE SUM OF DIGITS OF A NUMBER UNTILL THE NUMBER BECOME SINGLE DIGIT
# CHECK WHETHER SUM IS EVEN OR ODD

n=int(input("enter the num"))
sum = 0
while(n > 0 or sum > 9):
    if(n == 0):
        n = sum
        sum = 0
    sum += n % 10
    n //= 10
print(sum)
if sum%2==0:
    print("even")
else:
    print("odd")
    


    
