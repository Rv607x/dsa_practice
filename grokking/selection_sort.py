def find_smallest(arr):
    """Find index of smallest item in the array"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
#print(find_smallest([5, 3, 6, 2, 10]))

def selection_sort(arr):
    """Implementation of selection sort algorithm that creates a new empty array
    finds the smallest element in chosen array then pops it off and add to new array
    till all arrays are popped off"""
    new_arr = []
    copied_arr = list(arr)
    for i in range(len(copied_arr)):
        smallest = find_smallest(copied_arr)
        new_arr.append(copied_arr.pop(smallest))
    return new_arr
print(selection_sort([5, 3, 6, 2, 10, -6]))