# set={1,23,4,56,7,9,9,9}
# print(set)
# for i in set:
#     print(i)

# s={33,5,8,7,"gani","ertybt"}
# print(s)

# harry={}
# print(type(harry))

# SET METHODS
set={1,2,3,6}
set2={4,5,6}
print(set.union(set2))

set={1,2,3,6}
set2={4,5,6}
set3=set.update(set2)
print(set)

set={1,2,3,6}
set2={4,5,6}
set3=set.intersection(set2)
print(set3)

set={1,2,3,6}
set2={4,5,6}
set3=set.intersection_update(set2)
print(set3)

set={1,2,3,6}
set2={4,5,6}
set3=set.difference(set2)
print(set3)

set={1,2,3,6}
set2={4,5,6}
set3=set.symmetric_difference(set2)
print(set3)

set={1,2,3,6}
set2={4,5,6}
print(set.isdisjoint(set2))

set={1,2,3,6}
set2={1,2,3,4,5,6}
print(set2.issuperset(set))

set={1,2,3,4,5,6}
set2={4,5,6}
print(set2.issubset(set))

set1={1,2,3,4,5,6}
set2={7,8,9,10}
set1.update(set2 )
print(set1)

set={1,2,3,4,5,6}
set.add(7)
print(set)

set={1,2,3,4,5,6}
set.remove(6) #if there is no item which does not in the set it will show error  
print(set)

set={1,2,3,4,5,6}
set.discard(7) #no matter if the item not present in the set it will show the output without the showing the eerror
print(set)

set={1,2,3,4,5,6}
del set
print(set)
 
 
car={"honda","swift","lamborgini","maruthi"}
if "honda" in car:
    print("honda in car")
else:
    print('honda is not in car')