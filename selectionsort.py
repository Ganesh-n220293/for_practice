array=[]
size=int(input("enter the no of elements in the array:"))
for i in range(0,size):
    item=int(input(f"enter {i}th element:"))
    array.append(item)
print("before sorting:")
print(array)
def selectionsort(array):
    for i in range(size):
        min=i
        for j in range(i+1,size):
            if(array[j]<array[i]):
                min=j
            else:
                continue
        temp=array[i]
        array[i]=array[min]
        array[min]=temp
    print("after sorting:")
    print(array)
selectionsort(array)