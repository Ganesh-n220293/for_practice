def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = []
    greater = []

    # Build less and greater using a loop
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            less.append(arr[i])
        else:
            greater.append(arr[i])

    # Recursively sort the partitions
    return quick_sort(less) + [pivot] + quick_sort(greater)

# Example
arr = [8, 4, 7, 3, 5, 2, 6]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)