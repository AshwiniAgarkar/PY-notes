# # correct_password="1234"
# # attempts=0
# # while attempts<3:
# #     password=(input("enter your password : "))
# #     if correct_password==password:
# #         print("You have successfully logged in.")
# #         break
# #     else:
# #         attempts=attempts+1
# #         print("Incorrect password")
# # if attempts == 3:
# #     print("You have been denied access.")


# num1=float(input("Enter a number : "))
# num2=float(input("Enter a number : "))
# s=num1+num2
# if s>=100:
#     print("That is a big number")
    


# string = input("Enter a string : ")
# if string == string[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")



# weight=float(input("Enter your weight in kg : "))
# height=float(input("enter your height in m : "))
# BMI=weight/(height**2)
# print("your BMI is",BMI)



n = int(input("Enter the number of terms in Fibonacci series: "))  
a, b = 0, 1
print(a)

for i in range(1, n):
    print(b)
    a, b = b, a + b  
