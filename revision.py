# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
# c=input("enter the opertaion:")
# if(c=="*"):
#     print(a*b)
# elif(c=="+"):
#     print(a+b)
# elif(c=="-"):
#     print(a-b)
# elif(c=="**"):
#     print(a**b)
# elif(c=="/"):
#     if(b!=0):
#       print(a/b)
# elif(c=="//"):
#     if(b!=0):
#       print(a//b)
# elif(c=="%"):
#     if(b!=0):
#       print(a%b)

# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
# # print(a=b)
# print(a==b)
# print(a!=b)
# print(a>b)

# if(a>10 and b>10):
#    print("both are greater than 10")
# elif(a>10 or b<10):
#    print("one of the value is greater than 10")
# # else:
# #    print("both are less than 10")

# print(a&b)
# print(a|b)
# print(a^b)

# a="ganesh"
# print(a[0:3])
# print(a[0:])
# print(a[:4])
# print(a[:-1])
# print(a[-1::-1])
# print(a[::-1])

# a=90
# if(a>80):
#     print("webiwebfi")
# if(a<100):
#     print("hbfkyervfkyer")
# if(a<101):
#     print("hbfkyervfkyer")
# if(a<160):
#     print("hbfkyervfkyer")

# a=["rtretgret","rtertherth","rtyerththerth","erthertherthrethe"]
# for i in a:
#     print(i,"\n")
#     for j in i:
#         print(j)

# n=20
# i=0
# while(i<=20):
#     if(i==13):
#         print("pass the number")
#         continue
#     print(i)
#     i=i+1

# def average():
#     return 2

# average()

# name="gani"
# id="N220293"
# print(f"my name is {name} with id:{id}")

# f=open("sprighty.txt","w")
# print(f.write("webfyuegrfylegrlfyegrlfy \n"))
# f.close

# f=open("sprighty.txt","a")
# print(f.write("rjkfgejryfgeyirfgleruglegrliegr"))
# f.close


# f=open("sprighty.txt","r")
# print(f.read())
# print(f.seek(5))
# f.close

# x=lambda a:a**2
# print(x(5))

# def cube(a):
#     return a*a*a
# l=[1,2,3]
# print(list(map(cube,l)))

# def apple(a):
#     return a>4
# l=[1,2,3,566,755,7,8]
# print(list(filter(apple,l)))

# def sum(x,y):
#     return x+y
# l=[3445,657,66,5,7]
# print(reduce(sum,l))

# days=int(input("no.of working days:"))
# present=int(input("no.of days present:"))
# attendance=(present/days)*100
# if(attendance>=75):
#     print("yes")
# else:
#     print("no")

# years=int(input("enter the no.of years of service:"))
# salary=int(input("enter the salary:"))
# bonus=((10*salary)/100)+salary
# if(years>5):
#     print(bonus)
# else:
#     print("your not eligible for bonus")

# gender=str(input("enter the employee gender:"))
# age=int(input("enter age:"))
# martial_status=str(input("enter yes or no:"))
# M="male"
# F="female"
# if(gender==F and martial_status==f"yes"):
#     print("you can work in urbane places")
# if(gender==M and martial_status=="yes"):
#     if(20<age<=40):
#         print("you may work in anyplace")
#     elif(40<age<=60):
#         print("you can only work in urban places")
#     else:
#         print("ERROR")
# else:
#     print("ERROR")

# n=int(input("enter the value of n:"))
# for i in range(2,n+1):
#     for j in range(2,i):
#          if(i%j==0):
#               break
#     print(i)

# class ganibhai():
#     def __init__(self,name,id,value):
#      self.name=name
#      self.id=id
#      self.value=value
#     def info(self):
#         print(f"my name is {self.name} with id number {self.id}")
#     @property
#     def ten_value(self):
#         return 10*self.value
# a=ganibhai("gani","N220293",21)
# a.info()
# print(a.ten_value)

# class father():
#     def __init__(self,name):
#      self.name=name
#     def info(self):
#         print(f"my father name is {self.name}")

# class son(father):
#    def __init__(self,peru):
#       self.peru=peru
#    def properties(self):
#       print(f"my name is {self.peru} my father name is {self.name}")

# a=father("K.Venkata Ramana")
# a.info()
# d=son("K.Ganesh")
# d.properties()

# class employee():
#     def __init__(self):
#         self.__name="ganesh"
# a=employee()
# print(a._employee__name)

# class employee():
#     def __init__(self):
#         self.name="ganesh"
#     def _funname(self):
#         print(f"my name is {self.name}")
# class student(employee):
#     pass 
# a=employee()
# print(a.name)
# b=student()
# b._funname()

# class math():
#     @staticmethod
#     def add(a,b):
#         return a+b
# a=math.add(1,2)
# print(a)

# class employee():
#     company="Apple"
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def info(self):
#         print(f"my name is {self.name} working in the company {self.company} with {self.salary}")
# a=employee("ganesh",10000)
# a.info()
# b=employee("gani",20000)
# b.company="samsung"
# b.info()


# class employee():
#     company="Apple"
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def info(self):
#         print(f"my name is {self.name} working in the company {self.company} with {self.salary}")
#     @classmethod
#     def new_company(self,company):
#         self.company=company

# a=employee("ganesh",10000)
# a.info()
# print(employee.company)
# a.new_company("tesla")
# a.info()
# print(employee.company)
# a=[1,2,3,4,5,8]
# print(dir(a))

import time
init = time.time()
print(time.time()-init)