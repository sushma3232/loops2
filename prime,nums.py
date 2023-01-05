# print prime numbers 


# min = int(input(" Enter the Min"))
# max = int(input(" Enter the Max"))

# i = min
# while(i <= max):
#     count = 0
#     j = 2
#     while(j<= i//2):
#         if(i % j == 0):
#             count = count + 1
#             break
#         j = j + 1
#     if (count == 0 and i != 1):
#         print(i)
#     i=i+1


# # # print prime numbers and their sum
# min = int(input(" Enter the Min"))
# max = int(input(" Enter the Max"))
# sum=0
# i = min
# while(i <= max):
#     count = 0
#     j = 2
#     while(j<= i//2):
#         if(i % j == 0):
#             count = count + 1
#             break
#         j = j + 1
#     if (count == 0 and i != 1):
#         print(i)
#         sum=sum+i
#     i=i+1
# print(sum)



i=2

while i <= 100:
    j = 2
    while j < 100:
        if i%j == 0:
            break
        j += 1
    if i == j:
        print(i,end=',')
    i += 1
    
    
# num = int(input("Enter a number: "))
# i = 2

# while i <= num:
#     j = 2
#     while j < num:
#         if i%j == 0:
#             break
#         j += 1
#     if i == j:
#         print(i,end=',')
#     i += 1