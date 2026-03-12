# import os
# # if(not os.path.exists("data"))
#     #  os.mkdir("data")
# for i in range(0,100):
#     #  os.mkdir(f"day-{i}")
#      os.rename(f"tutorial-{i}"),f"tutorial-{i}"


import os
folders=os.listdir("costume")
print(folders)

for folder in folders:
    print(os.listdir(f"{folder}"))