#question 2
# num=int(input("enter a number : "))
# start=int(input("enter a start : "))
# end=int(input("enter a end : "))
# if start<=num<=end:
#         print("Its in range")
# else:
#         print("Not in range")


#question 3
# a = int(input("Enter a Number: "))
# if a <= 1:
#     print(a, "is Not Prime Number")
# else:
#     for i in range(2, a):
#         if a % i == 0:
#             print(a, "is Not Prime Number")
#             break
#     else:
#         print(a, "is Prime Number")

#question 4
# String=input("enter a string")
# if String==String[::-1]:
#     print("its a palindrome")
# else:
#     print("not a palindrome")

n = int(input("enter a no : ")) 
fact = 1
for i in range(1, n + 1):
    fact *= i

print("factorial of a number is",fact)
