# Creating a dictionary
empty_dict = {}
print(empty_dict)

phone_book = {"Batman": 42786,
              "Cersei": 76345,
              "Ghostbusters": 63778
              }
print(phone_book)

# dict() constructor
# used to construct a dictionary

empty_dict2 = dict() #create empty dictionary
print(empty_dict2)

phone_book2 = dict(Batman=42786, Cersei = 76345, Ghostbusters= 63778)
print(phone_book2)

# Alternative approach 
phone_book3 = dict([('Batman', 468426),
                   ('Cersei', 237734),
                   ('Ghostbusters', 44678)])
print(phone_book3)

# Accessing Dictionary values
print(phone_book3['Cersei'])

# can also use get() method by a_dictionary.get(key)
print(phone_book3.get("Cersei"))

# adding/ updating entries
phone_book3["Godzilla"] = 45687   # New Entry 
print(phone_book3)

phone_book3["Cersei"] = 56212   # Updating entry
print(phone_book3)

# Deleting entries
# use del keyword to remove entries
del phone_book3["Godzilla"]
print(phone_book3)

# To use deleted value, pop() or popitem() methods are used
cersei = phone_book3.pop("Cersei")
print(phone_book3)
print(cersei)

# Length of dictionary 
print(len(phone_book3))

# Checking for existance of key in dictionary
# use in keyword
print("Batman" in phone_book3)

# Copying dictionary components 
# Use update() operation

second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}
phone_book3.update(second_phone_book)
print(phone_book3)
