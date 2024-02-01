my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]

list2 = []
list2.append(my_list[0])
list2.append(my_list[-1])
list2.append(len(my_list))

my_tuple = tuple(list2)
print(my_tuple)
