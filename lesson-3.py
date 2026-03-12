# our name upto infinity
# n=int(input("enter a number"))
# i="ganesh"
# while(0<=n):
#     print(i)

# natural numbers upto n
# n=int(input("enter a number"))
# i=1
# while(0<=n):
#     print(i)
#     i=i+1

# even numbers upto n
# n=int(input("enter a number"))
# i=0
# while(i<=n):
#     if(i%2==0):
#      print(i)
#      i=i+2

# make sum of all items in a list
# def add(x,y):
#     return x + y

# l=[1,2345,5667,890]
# cat=reduce(add,l)
# print(cat)

# upto n natural numbers by for loop
# n=int(input("enter a number"))
# for i in range(0,n+1):
#     print(i)

# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     for i in range(i):
#         print("*",end='')
#     print()


# sum of odd numbers
# n=int(input("enter a number"))
# i=1
# s=0
# while(i<n):
#     if(i%2!=0):
#         s=s+1
#     i=i+1
# print(s)

# n=int(input("enter a number"))
# s=0
# for i in range(1,n+1):
#         if(i%2!==0):
#       s=s+1
# print(s)

# factorials for a given number
# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     if(n%i==0):
#         print("the factorials is",i)
#     i=i+1

# n=int(input("enter a number:"))
# i=1
# while(i<n+1):
#     if(n%i==0):  
#         print(i)
#         i=i+1

# # for entering some items in list by taking form user
# n=int(input("enter a number:"))
# s=[]
# for i in range(n):
#     print("enter a elemnt:"," ",end=" ")
#     i=i+1
#     element=int(input())
#     s.append(element)
# print(s)

# s=[23,34,23,67,78,89,45,67]
# ulist=[]
# dublist=[]
# for i in range(len(s)):
#     if s[i] not in ulist:
#         ulist.append(s[i])
#     else:
#         dublist.append(s[i])

# question1
# n=int(input("enter:"))
# for i in range(0,n):
#     print(i)
#     i=i-1   
# i=int(input("enter:"))
# while(i>0):
#     print(i)
#     i=i-1

# question2
# n=int(input("enter:"))
# for i in range(0,n,2):
#     print(i)
#     i=i+2

# while (0<n):
#     print(n)
#     n=n+2

# question3
# i=int(input("enter:"))
# s=0
# for i in range(0,i):
#     if(i%2!=0):
#         print(i)
#         s=s+1
#         i=i+1

# question4
# n=int(input("enter:"))
# for i in range(0,11):
#     print(f"{n}x{i}={n*i}")
        
# question5
# n=int(input("Enter a Number: ")) 
# sum=0 
# while(n>0): 
#  sum=sum+n%10 
#  n=n//10 
# print("sum of digits of given number is ",sum)

# question6
# n=int(input("Enter a Number to get Prime Numbers: ")) 
# print("Prime Numbers upto ",n," are: ",end="") 
# for i in range(2, n+1): 
#  for j in range(2,i): 
#   if(i%j==0): 
#    break 
#  else: 
#   print(i,", ", end="")

# question7
# n=int(input("enter the number:"))
# sum=0
# for i in range(1,n):
#     if(n%i==0):
#        sum=sum+i
# print(sum)i
# if(sum==n):
#          print(n,"is a perfect number")
# else:
#      print(n,"is not a perfect number")

# question 8
# n=int(input("enter the number:"))
# y=str(n)
# print("first digit=",y[0])
# print("last digit=",y[-1])


# n=int(input("enter the number:"))
# last_digit=n%10
# while(n>0):
#      first_digit=n%10
#      n=n//10
# print("last digit=",last_digit)
# print("first digit=",first_digit)

#  question 10
# for i in range(ord("A"),ord("Z")+1):
#     print(chr(i))

# question9
# k=int(input("enter the number:"))
# rev=0
# for k in range(1,k+1):
#     while(k!=0):
#         rem=k%10
#         rev=(rev*10)+rem
#         k=k//10
# print("revverse=",rev,end="")
# if(k==rev):
#     print(rev,"is a polindram")
# else:
#     print(rev,"is not a polyndram")

# question 11
# n=int(input("enter a number:"))
# n1=n
# arm=0
# l=len(str(n))
# while(n!=0):
#     rem=n%10
#     arm=arm+(rem**l)
#     n=n//10
# if(arm==n1):  
#     print(n1,"is a armstrong")
# else:
#     print(n1,"is not  armstrong number")

# question 12
# n=int(input("enter the number:"))
# sum=0
# r=len(str(n))
# for i in range():
#     rem=n%10
#     l=rem*(rem-1)
#     n=n//10
#     sum=sum+l
# print(sum)

s="dog"
print(enumerate(s),'\n')








# question13
# n=int(input("enetr the number:"))
# n1=0
# n2=1
# new_number=n2
# for i in range(n):
#     print(n1,end="")
#     new_number=n1+n2
#     n1=n2
#     n2=new_number

# question14
# n=int(input("enter the number:"))
# for i in range(0,n):
#     for i in range(i):
#         print("*",end="")
#     print()

# question 15
# n=int(input("enter the number:"))
# for i in range(0,n):
#     for i in range(i):
#         print(i,end="")
#     print()

# l=[223,45,65,44,54,64,54,53,53]
# print(len(l)) 