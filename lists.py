friends = ["Peter", "Petra", "Jim", "Olga", "Cami", "Benjamin"]
list = ["Peter", "20", "False"]

print(friends)
print(friends[1])
print(list[2])
print(friends[-1]) # last element
print(friends[1:]) # from index 1 to end
print(friends[1:3]) # from index 1 to 3

friends.extend(list) # friends + list

print(friends)

friends.append("Günther") # adds element to the end
friends.insert(1, "Karen") # inserts Karen to index 1

print(friends)

friends.remove("Olga")

print(friends)

#friends.clear()

print(friends.pop()) # removes last element and reads it
print(friends)
print(friends.index("Peter")) # returns the index of arg
print(friends.count("Jim")) # returns the

friends.sort() # sorts in alphabetical order
print(friends)

friends.reverse() # sorts in reverse order
print(friends)

friends2 = friends.copy() # copies list
print(friends2)