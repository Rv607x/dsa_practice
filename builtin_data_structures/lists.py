#creating a list 
john_snow = ["john Snow", "Winterfell", 30] 
print("list items are:", john_snow)

#indexing a list 
print("last item in list is:", john_snow[-1])

# Length of list 
print("length of list is", len(john_snow))

# Lists are mutable hence their values can be changed 
john_snow[2] += 3
print(john_snow[2])

# a range can be converted to lists using list casting method 
num_seq = range(0, 10)
num_list = list(num_seq)
print("Number range is:", num_list)

num_seq = range(3, 20, 3)
print("A sequence from 3-29 with a step of 3 is:", list(num_seq))

# List-ception is nesting of lists in other lists
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print("World cup winners lst is", world_cup_winners)

# Merging of lists 
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
merged_list = part_A + part_B
print("merged list is:", merged_list)

# Adding elements to lists
# append() method is used to add elements to end of lists
my_list = [] # innitialize empty list to add elements to it
my_list.append(1)
my_list.append(2)
my_list.append(3)
print("new list with appended data is:", my_list)

# Adding elements at certain indexes in lists
# to add element at particular index in a list, insert() keyword is used
# insert is used using the format aList.insert(index, newElement)
new_list = [1, 2, 3, 5, 6]
new_list.insert(3, 4)
print("new list with inserted element is:", new_list)

# Removing Elements in list
# pop() keyword removes the last element in a list
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop() #variable with the popped element 
print("removed last element of list is:", last_house)
print("List with removed last elemt is:", houses)

# remove() keyword is used to delete element at particular index
# used the format aList.remove(element_to_be_deleted)
houses2 = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
print("Original list is:", houses2)
houses2.remove("Ravenclaw")
print("List with ravenclaw elementt removed is:", houses2)

# list slicing
# List Slicing gives a sublist
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5]) # prints 3rd to 5fth element in list
print(num_list[0::2]) # Prints every 2nd element from the first

# Index search
# use index() method to search for an element in list
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print(cities.index("Los Angeles"))  # It is at the 2nd index

# use "in" to verify if element exists in a list
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print("London" in cities)
print("Moscow" not in cities)

# List sort
# User sort() method to sort a list
num_list2 = [20, 40, 10, 50.4, 30, 100, 5]
num_list2.sort()
print(num_list2)

# List Comprehension
# is a technique to create a new list using for loop
# list comprehension statement always enclosed in []
# consists of 3 main parts: [expression, for loop and if condition]
nums = [10, 20, 30, 40, 50]
nums_double = []
for n in nums:
    nums_double.append(n*2)
print(nums)
print(nums_double)

# using list comprehension, this can be shortened into
nums2 = [10, 20, 30, 40, 50]
nums_double2 = [n * 2 for n in nums2]
print(nums2)
print(nums_double2)
# adding an if condition
nums_double2_divisible_by4 = [ n * 2 for n in nums2 if n % 4 == 0]
print(nums_double2_divisible_by4)

#using multiple lists
list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]
sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]
print(sum_list)