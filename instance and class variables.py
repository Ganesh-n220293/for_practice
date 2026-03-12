class employee:
    company_name="apple"    
    def __int__(self,name):
        self.name=name
        self.raise_amount=0.02
    def showdetails(self):
        print(f"the employee name is{self.name} and his raise amount is{self.raise_amount} in {self.company_name} company")
emp1=employee("gani")
emp1.showdetails()
emp1.company_name="samsung"
print(employee.company_name)
# employee.showdetails(emp1)
emp2=employee("ganesh")
emp2.company_name="lava"
emp2.showdetails()