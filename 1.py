# # x=(1,23,45,6)
# # temp
# # x.append(67)
# # print(x)

# king=[7,6,9,80,5,6,6.5]
# print(king[1])

# x=input("enter a number:")
# print("you enetered:",x)

# x = int(input("enter your marks:"))
# if(x>90):
#     print("your grade is excellent")
# elif(x>80 and x<90):
#     print("your grade is A")
# elif(x>70 and x<80):
#     print("your grade is B")
# elif(x>60 and x<70):
#     print("your grade is C")
# elif(x>50 and x<60):
#     print("your grade is D")
# elif(x>40 and x<50):
#     print("your grade is E")
# else:
    # print("you are failed")


# a = int(input("enter the value of a:"))
# b = int(input("enter the value of b:"))
# c = int(input("enter the value of c:"))
# if(a>b and a>c):
#     print("a is the biggest number")
# elif(c>b and c>a):
#     print("c is the biggest number")
# else:
#     print("b is biggest number")


# # printing factors
# n=int(input("enter the number"))
# f=0
# for i in range(1,n+1):
#          if(n%i==0):  
#               f=f+1
#               print(i)
# print("factors is:",f)

# perfect number
# a=int(input("enter the value of a:"))
# for n in range(1,a):
#     # n=int(input("enter the number"))
#     f=0
#     for i in range(1,n):
#             if(n%i==0):  
#                 f=f+i
#     if(f==n):
#         print(n,"is a perfect number")
#     else:
        # print(n,"is not a perfect number")
    
# reversing a number
# n=int(input("enter the number:"))
# rev=0
# while(n!=0):
#      rem=n%10
#      rev=(rev*10)+rem
#      n=n//10
# print("revverse=",rev)

# polindram
# a=int(input("enter the number:"))
# for n in range(1,a):
#     n1=n
#     rev=0
#     while(n!=0):
#         rem=n%10
#         rev=(rev*10)+rem
#         n=n//10
#     print(rev)


# armstrong
n=int(input("enter a number:"))
n1=n
arm=0
l=len(str(n))
while(n!=0):
    rem=n%10
    arm=arm+(rem**l)
    n=n//10
    if(arm==n1):  
        print(n1,"is a armstrong")
    else:
        print(n1,"is not  armstrong number")
            



