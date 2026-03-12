array=[]
size=int(input("enter the no of elements in the array:"))
for i in range(0,size):
    item=int(input(f"enter {i}th element:"))
    array.append(item)
print("before sorting:")
print(array)
def insertionsort(array):
    for i in range(1,size):
        key=array[i]
        j=i-1
        while(j>=0 and array[j]>key):
                   array[j+1]=array[j]
                   j=j-1
        array[j+1]=key
    print("before sorting:")
    print(array)

insertionsort(array)