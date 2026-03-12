# single inheritance
# class Animal():
#     def __int__(self,name,species):
#       self.name=name
#       self.id = species
#     def make_sound1(self):
#       print(f"sound made by the animal {self.name}")

# class Dog(Animal):
#    def __init__(self,name):
#       self.name=name
#    def make_sound():
#       print("bark!")

# d=Dog("dog")
# d.make_sound1() 

# multiple inheritance  
# class name:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"the dancer name is {self.name}")
# class dance:
#     def __init__(self,dance):
#         self.dance=dance
#     def show1(self):
#         print(f"the dance name is {self.dance}")
# class namedance(name,dance):
#     def __init__(self,name,dance):
#         self.name=name
#         self.dance=dance
#     def show2(self):
#         print(f"{self.name} is expert in {self.dance} dance")

# q=namedance("brighty","kuchipudi")
# q.show2()
# q.show()
# q.show1()

# multilevel inheritance
class Animal():
    def __int__(self,name,species):
      self.name=name
      self.species=species
    def show_details(self):
      print(f"name:{self.name}")
      print(f"species:{self.species}")

class dog(Animal):
   def __init__(self,breed):
      self.breed=breed
   def show_details(self):
      Animal.show_details(self)
      print(f"breed:{self.breed}")

class goldenretriever(dog):
   def __init__(self,name,color,species,breed):
      self.name=name
      self.color=color
      self.species=species
      self.breed=breed
   def show_details(self):
         dog.show_details(self)
         print(f"color:{self.color}")

g=goldenretriever("tommy","black","dog","goldenretriever")
g.show_details() 