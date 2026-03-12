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