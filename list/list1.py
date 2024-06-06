from itertools import combinations_with_replacement

# Given lists
list1 = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
list2 = ['B', 'B', 'B', 'B', 'B', 'B', 'B']
list3 = ['C', 'C', 'C', 'C', 'C', 'C', 'C']

# Concatenate the lists
all_elements = list1 + list2 + list3

# Generate all possible combinations of 12 elements
all_combinations = combinations_with_replacement(all_elements, 12)

# Create a set to store unique combinations
unique_combinations = set()

# Iterate through all combinations and add unique ones to the set
for combination in all_combinations:
    unique_combinations.add(tuple(sorted(combination)))

# Convert the set of unique combinations to a list of lists
list_of_lists = [list(combination) for combination in unique_combinations]

# Print the list of lists
for inner_list in list_of_lists:
    print(inner_list)
