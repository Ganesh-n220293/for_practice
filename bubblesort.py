array=[]
size=int(input("enter the no of elements in the array:"))
for i in range(0,size):
    item=int(input(f"enter {i}th element:"))
    array.append(item)
print("before sorting:")
print(array)
def bubblesort(array):
    for j in range(size):
     for k in range(size-j-1):
        if(array[k]>array[k+1]):
            temp=array[k]
            array[k]=array[k+1]
            array[k+1]=temp
        else:
            continue
    print("after sorting:")
    print(array)
bubblesort(array)
