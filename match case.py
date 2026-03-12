# x = int(input("enter the number:"))
# match x:
#     case 0:
#         print("x is zero")
#     case 8:
#         print("x is eight")
#     case _:
#         print(x)


x = int(input("enter the number:"))
match x:
    case 0:
        print("x is zero")
    case 8:
        print("x is eight")
    case _ if x!=20:
        print(x,"is not equal to 20")
    case _:
        print(x)
