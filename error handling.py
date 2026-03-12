# try expect method
# a=int(input("enter a number:"))
# print(f"multiplication table of {a} is")
# try:
#    for i in range(0,11):
#      print(f"{int(a)}x{i}={int(a)*i}")
# except ValueError:
#    print("print number perfectly")

# print("enetr a number perfectily")
# print("try another one")

# finally
# def func1():
#   try:
#    l=[1,3,4,5,6,7]
#    i=int(input("enter the index you want:"))
#    print(l[i])
#   except:
#    print("enter th right one")
   
#   finally:
#     print("enter something else")

# x=func1()
# print(x)

a=int(input("enter a number betwwen 5 and 9:"))
if(a<5 or a>9):
  raise ValueError("value should be between 5and 9")