# def cat(a,b):
#     mean=(a*b)/(a+b)
#     print(mean)

# def isgreater(a,b):
#     if(a>b):
#         print("a is greater")
#     else:
#         print("b is greater")
# a=90
# b=100
# cat(a,b) 
# isgreater(a,b)

# c=89
# d=199
# cat(c,d)
# isgreater(c,d)

# RECURSION FUNCTION
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))


# def add(a,b,c):
#     x=a+b+c
#     print(x)
# add(5,6,7)

unit=100
no_of_units=int(input("enter"))
cost=unit*no_of_units
a=(10/cost)*100
if(cost>1000):
    print(cost-(a))
else:
    print("your no eligible fo discout")


# def add(name,id,department="puc"):
#     print("name is",name)
#     print("id is",id)
#     print("cls is",department)
#     # name=str(input("enetr the name"))
#     # id=str(input("enter your id"))
#     # department=str(input("enter your department name"))
# add(name="gani",id="n220293",department="puc")