# Creating a set
random_set = {"Cow", 2345, 56.76, (True, False)}
print(random_set)
print(len(random_set))

# Set constructor 
# set() is another way of creating a set

empty_set = set()
print(empty_set)

random_set2 = set({"Cow", 2345, 56.76, (True, False)})
print(random_set2)

# Adding elements to set
# to add single item add() method is used, to add multiple update()method is used
empty_set.add(1)
print(empty_set)

empty_set.update([2, 3, 4, 5, 6])
print(empty_set)


# Set theory operations
########################
# Union - Collection of unique elements from both sets
# In Python, union can be performed using either the pipe operator, |, or the union() method
set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c', 'd'}

print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))

# Intersection - The intersection of two sets is the collection of unique elements which are common between them.
# In Python, intersection can be performed using either the & operator or the intersection() method:
set_C = {2, 8, 4, 16}
print(set_A & set_C)
print(set_A.intersection(set_C))
print(set_C.intersection(set_A))