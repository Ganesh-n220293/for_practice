# public
# class Employee:
#     def __int__(self):
#         self.name="ganesh"
# obj=Employee()
# print(obj.name)

# private modifiers
# class Employee:
#     def __int__(self):
#         self.__name="ganesh"
# obj = Employee()
# print(obj.__name)

# protected
class student:
    def __int__(self):
        self.__name="ganesh"
    def __functionname__(self):
        return "code with harry"
class subject(student):
     pass
obj = student()
obj1=subject()
print(obj._name)
print(obj._funname)
print(obj1._name)
print(obj1._funname)