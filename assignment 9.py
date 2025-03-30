# # #QUESTION 1
# # base=float(input("enter value for base : "))
# # exponent=float(input("enter value for exponent : "))
# # answer=base**exponent
# # print(base ,"raised to the power of", exponent,"is",answer)

# #QUESTION 2
# # num = int(input("Enter a number: "))
# # a, b = 0, 1
# # while a < num:
# #     a, b = b, a + b
# # if a == num:
# #     print("Great")
# # else:
# #     print("Oops, it's wrong")


# #QUESTION 3
# # num=int(input("enter a num"))
# # binary_resp = bin(num)[2:]
# # if  binary_resp==binary_resp[::-1]:
# #     print("its a palindrom ")
# # else:
# #     print("not a palindrome")

#QUESTION 5
# sum=0
# for i in range(1,1000):
#     if i%2==0 or i%4==0:
#         sum=sum+i
# print(sum)



N = int(input("Enter the value of N: "))
count = 0
for i in range(1, N + 1):
    if '0' in str(i):  
        count += 1
print("the number of integers from 1 to ",N, "that contain atleast 1 zero is ", count)