def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(arr[1], len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest

#print(findSmallest([6, 0, 2, 9]))

def selectionSort(arr):
    sorted_arr = []
    copied_arr = list(arr)
    for i in range(len(copied_arr)):
        smallest = findSmallest(arr)
        sorted_arr.append(copied_arr.pop(smallest))
    return sorted_arr

print(selectionSort([6, 0, 2, -9]))