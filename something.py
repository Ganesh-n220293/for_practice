# # p=True
# # q=False
# # print(p or q)
# # print(p and q)
# # print((not p) or q)
# # print(((not p) or q) and ((not q) or p)) 

# # def conjuction(p,q):
# #         if(p==True and q==False):
# #             print(p and p) 
# #             print(p and q)
# #             print(q and p)
# #             print(q and q)
# #         else:
# #             print(q and q) 
# #             print(q and p)
# #             print(p and q)
# #             print(p and p)

# # conjuction(p,q)
# # A=[]
# # def conjuction(A):
# #   A=[True,False]
# #   for p in A:
# #     for q in A:
# #         if(p and q):
# #             print(p,q,True)
# #         else:
# #             print(p,q,False)

# # conjuction(A)

# # A=[]
# # def disjunction(A):
# #   A=[True,False]
# #   for p in A:
# #     for q in A:
# #         if(p or q):
# #             print(p,q,True)
# #         else:
# #             print(p,q,False)

# # disjunction(A)

# # A=[]
# # def implication(A):
# #   A=[True,False]
# #   for p in A:
# #     for q in A:
# #         if((not p) or q):
# #             print(p  ,q  ,  True)
# #         else:
# #             print(p  ,q  ,False)

# # implication(A)

# # A=[]
# # def biconditional(A):
# #   A=[True,False]
# #   for p in A:
# #     for q in A:
# #         if(((not p) or q) and ((not q) or p)):
# #             print(p,q,True)
# #         else:
# #             print(p,q,False)

# # biconditional(A)


# a=[True,False]
# def implies(p,q):
#             if((not p) or q):
#                 return True
#             else:
#                 return False


# def bicond(p,q):
#             if(((not p) or q) and (not q) or p):
#                 return True
#             else:
#                 return False
# for p in a:
#         for q in a:
#             if(implies(p,q) and (not q) and bicond(p,q)):
#                  print(p,q,True)
#             else:
#                  print(p,q,False)

# operand1=int(input("enter operand1:"))
# operand2=int(input("enter operand2:"))
# a=input("enter the operation u want to perform:")
# if(a=='+'):
#     print(operand1+operand2)
# if(a=='-'):
#     print(operand1-operand2)
# if(a=='*'):
#     print(operand1*operand2)
# if(a=='/'):
#     if(operand2!=0):
#         print(operand1/operand2)
#     else:
#         print("we cannot perfrom division")
# if(a=='%'):
#     if(operand2!=0):
#         print(operand1%operand2)
#     else:
#         print("we cannot perfrom modulos operation")


# stack=[]
# def push(a):
#     stack.append(a)
# def peek(stack):
#     print()

# import numpy as np
# stack=np.array([1,2,3,4])
# print(stack)

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6][7,8]])
c=a.dot(b)
print(c)