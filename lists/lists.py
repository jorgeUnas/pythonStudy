# Your code below: 

# Checkpoint 1
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

# Checkpoint 2
preferred_size = ["Small", "Large", "Medium"]

# Checkpoint 3
preferred_size.append("Medium")
print(preferred_size)

# Checkpoint 4
customer_data = [["Ainsley", "Small", True ], ["Ben", "Large", False ], ["Chani", "Medium", True ], ["Depak", "Medium", False ]]
print(customer_data)

# Checkpoint 5
customer_data[2][2] = False

# Checkpoint 6
customer_data[1].remove(False)

# Checkpoint 7
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)


# Combining lists 

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)