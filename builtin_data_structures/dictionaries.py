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
