# creating a file
# f=open("write2.txt","x")

# reading
# f=open("write.txt","a")
# fruit=f.read()
# print(fruit)
# f.close()

# writting
# f=open("write.txt","w")
# fruit=f.write("hello world")
# print(fruit)
# f.close()

# appending
# f=open("write.txt","a")
# fruit=f.read("write")
# print(fruit)
# f.close()

# with open("write.txt","w"):
#     write("hey there iam using whatsapp")

# # readline()
# f=open("write.txt","r")
# # while True:
# line=f.read()
# #   if not line:
#     #   break
# print(line)
# f.close()

# seek() function
f=open("write.txt","r")
first=f.seek(10)
data=f.read(5)
print(first)
print(data)