from itertools import product

# Given lists
list1 = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
list2 = ['B', 'B', 'B', 'B', 'B', 'B', 'B']
list3 = ['C', 'C', 'C', 'C', 'C', 'C', 'C']

# Generate all possible combinations of elements from the lists
all_combinations = product(list1, list2, list3, repeat=1)

# Create a set to store unique combinations
unique_combinations = set()

# Iterate through all combinations and add unique ones to the set
for combination in all_combinations:
    unique_combinations.add(tuple(sorted(combination)))

# Convert the set of unique combinations to a list of lists
example_list = [list(combination) for combination in unique_combinations]

# Print the list of lists
for inner_list in example_list:
    print(inner_list)
