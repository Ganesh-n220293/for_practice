# class parent():
#     def parent_method(self):
#         print("this is parent")
# class child(parent):
#     def parent_method(self):
#         print("harry")
#         super().parent_method()
#     def child_method(self):
#         print("this is child")

# s=child()
# s.child_method()
# s.parent_method()

# class employee():
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
# class programmer(employee):
#     def __init__(self,name,id,lang):
#         super().__init__(name,id)
#         self.lang=lang

# s=employee("gani",300)
# print(s.name)
# print(s.id)
# k=programmer("gani",300,"python")
# print(k.name)
# print(k.id)
# print(k.lang)