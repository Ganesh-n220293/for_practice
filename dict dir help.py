# dir()
# x=[1,2,3,4,5]
# print(dir(x))
# print(x.__add__)

# __dict__
class person():
    def __init__(self,name,age):
     self.name=name
     self.age=age
p=person("gani",18)
print(p.__dict__)

# dict
print(help(person))
