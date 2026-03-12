# class person():
#     name="ganesh"
#     age=18
#     professsion="student"
#     def info(self):
#         print(f"{self.name} is {self.age} years old")
# a=person()
# # print(a.name)
# name="gani"
# age=27
# print(a.name,a.age)
# a.info

# constructors
class person:
    def __int__(self,n,o):
        self.name=n
        self.occ=o
        
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=print("harry","developer")
b=print("gani","hacker")
a.info()
b.info()