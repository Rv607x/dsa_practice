# Simmilar to lists except the contents are immuatable or cannot be changed

# creating a tuple
car = ("Ford", "Raptor", 2019, "Red")
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")

print(hero1)
#lenght of tuple
print(len(hero1))

#indexing a tuple
print(car[1])

#slicing a tuple 
print(car[2:])

# Merging Tuples
awesome_team = hero1 + hero2
print(awesome_team)   

#nested Tuple
awesome_team_nested = (hero1, hero2)
print(awesome_team_nested)

# Search tuples
# Use in operator
print("Batman" in hero1)