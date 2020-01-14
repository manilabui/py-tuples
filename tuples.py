#zoo
zoo = ("panda", "python", "alpaca", "mouse", "whale", "gibbon", "tiger", "lion", "leopard", "guinea pig")
print(zoo.index("alpaca"))

animal_to_find = "python"
if animal_to_find in zoo:
    # Print that the animal was found
    print(f'{animal_to_find} was found')

# Create a variable for the animals in your zoo tuple, and print them to the console.
# You have to put all of the variables in, else it don't work, dawg.
(first_animal, second_animal, third, fourth, fifth, sixth, seventh, eighth, nineth, tenth) = zoo
print(first_animal)
print(second_animal)

# Convert your tuple into a list.
zoo = list(zoo)
print(zoo)

# Use extend() to add three more animals to your zoo.
zoo.extend(["ferret", "gerbil", "platypus"])
print(zoo)

# Convert the list back into a tuple.
zoo = tuple(zoo)
print(zoo)