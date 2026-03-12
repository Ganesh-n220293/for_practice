# dic={"king":"gani","queen":"still in searching",500:"narendra"}
# print(dic)
# print(dic["king"])
# print(dic[500])
# print(dic.get('ganesh'))
# print(dic.get"ganesh") 
    #   if the given element does not contain
    #  in dictinary it dont show error it will show the "none"
# print(dic.keys())
# print(dic.values())
# for i in dic.keys():
#     print(dic[i])
# print(dic.items())
#  for key,values in dic.items():
    # print({key},{value})

# dictionary methods
# update()
king={1:50,2:100,3:150,4:200,5:250,6:300}
queen={7:350,8:400,9:450,10:500}
king.update(queen)
print(king)
king.update({11:550})
print(king)

# clear()
king={1:50,2:100,3:150,4:200,5:250,6:300}
king.clear()
print(king)

# pop()
king={1:50,2:100,3:150,4:200,5:250,6:300}
king.pop(1)
print(king)

# popitem()
king={1:50,2:100,3:150,4:200,5:250,6:300}
king.popitem()
print(king)

# del()
king={1:50,2:100,3:150,4:200,5:250,6:300}
del king[1]
print(king)   