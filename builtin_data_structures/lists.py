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