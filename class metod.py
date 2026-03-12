# class employee:
#     company="apple"
#     def show(self):
#         print(f"the employee name is {self.name} in {self.company}company")
#     @classmethod
#     def changecompany(cls,newcompany):
#         cls.company=newcompany
# e1=employee()
# e1.name="harry" 
# e1.show()
# e1.changecompany("tesla")
# e1.show()
# print(employee.company) 

# using class method as altenative constructor
  
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def gani(self):
        print(f"{self.name} working in in the apple company for {self.salary} salary")
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

# e=employee("harry",12000)
# e.gani()

# string="gani-12000-python"
# e2=employee(string.split("-")[0],string.split("-")[1])
# e2.gani()

string="gani-12000-python"
e3=employee.fromstr(string)
e3.gani()