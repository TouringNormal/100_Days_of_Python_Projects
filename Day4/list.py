states_US = ["Delaware", "Pennsylvania", "Washington", "West Virginia", "Wisconsin"]

# entries in the list are at the same order as put into the list

states_US[1] = "Hawaii" #this changes a specific list item

states_US.append("Ohio") # "append" adds item to the end of the list

states_US.extend(["North Carolina", "Santa Carolina", "Maryland"]) #adds a list to the end of the list

print(states_US[1], states_US[3], states_US[-2])
print(states_US)