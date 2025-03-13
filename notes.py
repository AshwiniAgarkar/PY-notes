# a=int(input("enter a"))
# b=int(input("enter b"))
# sum=a+bve
# if sum>=100:
#     print("No. is big")

# for i in range(1500,2700):
#     if i%7==0 and i%5==0:
#         print(i)

# wap to check attemps for password and if 3 attempts are done them 
# print "you have exceeded the limit"

# correct_password="pass123"
# attempts=0
# while attempts<3:
#     enter_password = input("enter your password :")
#     if enter_password==correct_password:
#         print("you have logged in succesfully")
#         break
#     else:
#         print("incorrect password")
#         attempts=attempts+1
# if attempts==3:
#     print("you have been denied access")


# for i in range(1,50,1):
#     if i%3==0 and i%5==0:
#         print("fizzBuzz")
#     elif i%3==0:            
#         print("fizzz")
#     elif i%5==0:               
#         print("buzzz")
#     else:
#         print(i)
 

# alphabet=input("enter an alphabet :")
# if alphabet in'aeiouAEIOU':
#          print("Its a voWel")
# else:
#         print("Its a consonents")


# a=int(input("enter angle a"))
# b=int(input("enter angle b"))
# c=int(input("enter angle c"))
# if a+b+c==180:
#     if a==b==c:
#         print("Its an eqilatral triangle")
#     if a==b or b==c or c==a:
#         print("Its an isocelus triangle")
#     if a!=b and b!=c and c!=a:
#         print("Its scalene triangle")
# else:
#     print("not a triangle")



# a,b=0,1
# Print (Fibonacci series between 0,50:-)

# While a<=50:

# Print (a)
# a,b=b,a+b


# def evenodd(n):
#     if n%2==0:
#       print("even")
#     else:
#         print ("odd")
# n=int(input("enter a no. :"))
# evenodd(n)
        

# horsemen=["war","femine","pestilense","death"]
# i=0
# while i< 4:
#     print (horsemen[i])
#     i=i+1



# # horsemen=["war","femine","pestilense","death"]
# for i in horsemen:
#     print(i)

# LIST=["a","b","c","d","e","f"]
# print(LIST[1:3])

# fruit=["banana","apple","orange"]   #list are mutable
# fruit[1]="pear"
# fruit[-1]="jackfruit"
# print(fruit)

# list=['1','2','3','4','5','6','7','8']
# list[3:5]=['x','y']
# print(list)

# list=['1','2','3','4','5','6','7','8']
# list[1:1]=["z","y","x"]
# print(list)

#=['1','2','3','4','5','6','7','8']
# del list[1:6]
# print(list)

# list=['1','2','3','4','5','6','7','8']
# del list[1]
# print(list)

# a=[1,2,3]       #since and b are same so cahnges made in one will indirectly affectthe othe
# b=a
# b[1]="apple"
# print(a)
  
# a=[1,2,3,[5,6,7,8]]    #this is called nested list
# print(a[3])

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# matrix[2]
# print(matrix[1][1])


# song="the rain in spain...."    #conversion of string into list
# print(song.split())


# song=['the' ,'rain' ,'in','spain']      #conversion of list into string
# print( " ".join(song))


# fruit="jackfruit"
# for i in fruit:
#    print(i)

# fruit="jackfruit"
# for i in range(0,len(fruit)):
#    print(i)

# fruit="orange"      #string slicing
# print(fruit[1:])
# print(fruit[:])
# print(fruit[::-1])     #it reverses a string


# fruit="orange"
# count=0
# for i in fruit:
#     if i=="a":
#          count+=1
# print(count)


# from string import *
# fruit="banana apple orange kivi "
# print(fruit.find("i"))



#lists
#  l=[1,2,3,4,5]     #concatenation
# m=[6,7,8,9,0]
# a=l+m
# print(a)tring=input("enter a string : ")
# string=string.lower()

# list=[ ]
# print(list)

# list=["string", 4.4,8,0]    #hetrogeneus lsit
# print(list)
# print(list[2])

# a=[1,2,3,4,5]
# print(5 in a)
# a[3]="apple"
# print(a)
# del a[4]
# print(a)
# a.clear()     #gives an empty list
# print(a)
# # del a          #delete a entire list
# a.append(2000)     #to add only single elemnet
# print(a)
# a.extend([40,5,67,89])    #to add more than one element
# print(a)
# a.insert(3,3000)    #at position 3 3000 is inserted to print at any loaction we want
# print(a)
# a.sort()



#tuple  is immutable
# append,add,insert,remove does not work here
#convert tuple into list to make changes
#comple tuple can be deleted (del) but not a single element

# t=(100,5,8,9)
# x,y,z,d=t
# print(x)
# print(z)
# print(max(t))
# print(min(t))
# print(t.count(5))

#STRING IN BUILT METHODS
#string is immutable
s="    _rain in spain123_"
# print(s.upper())
# print(s.capitalize())
# print(s.lower())
# print(s.title())
# print(s.isupper())  #to check
# print(s.islower())
# print(s.istitle())
# print(s.casefold())
# print(s.count("r"))
# print(s.endswith("in"))
# print(max(s))
# print(s.center (40))
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.isidentifier())
# print(s.split())
# print("".join(s))
# print(s.rstrip())
# print(s.lstrip())
# print(s.find("a"))    #from forward
# print(s.rfind("a"))    #from backward
# print(s.swapcase())
# print(s.replace("spain","paris"))


#dictionary
d={1:"apple",2:"orange",3:{4:"mango"}}
print(d[2])
print(d[3])
print(d.keys())
print(d.values())
print(d.pop(1))