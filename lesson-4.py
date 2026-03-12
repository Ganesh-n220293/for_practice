# n=int(input("enter the lenght of the list:"))
# l=[]
# for i in range(0,n+,):
#     x=int(input(f"enter the element{0}="))
#     l.append(x)
# print(l)

# l=[32,34,5,44,65,44,55,45]
# l[2]=4
# print(l)

# l=[12,34,5,44,65,44,55,45]
# for i in l:
#     print(i)

# l=[12,34,5,44,65,44,55,45]
# print(3*l)

# list methods
# append
# l=[1,2,3,4]
# l.append(67)
# print(l)

# extend
# l=[12,34,5,44,65,44,55,45]
# d=[23,55,67,88,99,99,67]
# l.extend(d)
# d.extend(l)
# print(l)
# print(d)

# insert
# l=[12,34,5,44,65,44,55,45]
# l.insert(2,6)
# print(l)

# remove
# l=[12,34,5,44,65,44,55,45]
# l.remove(34)
# print(l)

# clear
# l=[12,34,5,44,65,44,55,45]
# l.clear()

# pop
# l=[1,23,34,56,67,7,66,66,5,5]
# l.pop()
# print(l)

# count()
# l=[1,23,34,56,67,7,66,66,5,5]
# print(l.count(5))

# sort()
# l=[1,23,34,56,67,7,66,66,5,5]
# l.sort()
# print(l)

# sort(reverse=true)
# l=[1,23,34,56,67,7,66,66,5,5]
# l.sort(reverse=True)
# print(l)

# reverse
# l=[1,23,34,56,67,7,66,66,5,5]
# l.reverse()
# print(l)

# copy
# l=[1,23,34,56,67,7,66,66,5,5]
# l2=l.copy()
# l2[0]=0
# print(l2)

# list comprehesion
# l=[2*x for x in range(10)]
# print(l)

# list membership
# l=[1,23,34,56,67,7,66,66,5,5]
# print(2 in l)

# build in fuctionsp
# l=[1,23,34,56,67,7,66,66,5,5]
# print(len(l))
# print(max(l))
# print(min(l))
# print(sum(l))
# print((sum(l))/len(l))

# user taking list and finding the average of the list and max and min value
# n=int(input("enter the lenght of the list:"))
# l=[]
# sum=0
# for i in range(0,n+1):
#     x=int(input("enter the element="))
#     l.append(x)
#     sum=x+sum
# print("list=",l)
# print(max(l))
# print(min(l))
# print("average=",sum/n)

# removing duplicate elements in the list and dd them to another list
# l=[23,343,45,676,8,9,887,7676,8,8]
# k=[]
# for i in l:
#     if(l.count(i)>1):
#         l.remove(i)
#         k.append(i)
# print(l)
# print(k)

# sum of elements in a list
# n=int(input("enter the lenght of the list:"))
# l=[]
# sum=0
# for i in range(0,n):
#     x=int(input(f"enter the element{0}="))
#     l.append(x)
#     sum=sum+x
# print(l)
# print(sum)

# n=123456789
# y=str(n)
# l=[]
# for i in y:
#     l.append(i)
# print(l)

# n="RGUKT RK VALLEY"
# l=[]
# for i in n:
#     l.append(i)
# print(l)


# tuple
# l=(12,44,55,7,78)
# for l in l:
#     print(l)

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

result = [[0, 0],
          [0, 0]]

for i in range(len(A)):         
    for j in range(len(B[0])):  
        for k in range(len(B)):  
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(row)



import numpy as np

def add(A, B):
    return A + B

def subtract(A, B):
    return A - B

def strassen(A, B):
    n = A.shape[0]

    # Base case: 1x1 matrix
    if n == 1:
        return A * B

    # Divide the matrices into quarters
    mid = n // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    # Strassen’s 7 multiplications
    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, subtract(B12, B22))
    M4 = strassen(A22, subtract(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(subtract(A21, A11), add(B11, B12))
    M7 = strassen(subtract(A12, A22), add(B21, B22))

    # Compute C submatrices
    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    # Combine submatrices into one
    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    return np.vstack((top, bottom))


A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 1, 2, 3],
              [4, 5, 6, 7]])

B = np.array([[7, 6, 5, 4],
              [3, 2, 1, 0],
              [8, 7, 6, 5],
              [4, 3, 2, 1]])

result = strassen(A, B)
print("Strassen Matrix Multiplication Result:")
print(result)