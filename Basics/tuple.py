tea_types = ('black', 'green', 'herbal', 'oolong', 'white', 'chamomile')
print(tea_types)
print(tea_types[0])  # Accessing the first element
print(tea_types[-1])  # Accessing the last element
print(tea_types[1:4])  # Slicing the tuple
print(len(tea_types))  # Length of the tuple
for tea in tea_types:
    print(tea)  # Iterating through the tuple
# tea_types[0] = 'matcha'  # This will raise a TypeError since tuples are immutable
print(tea_types.index('herbal'))  # Finding the index of an element
print(tea_types.count('green'))  # Counting occurrences of an element
# Concatenating tuples
more_teas = ('matcha', 'chai')
all_teas = tea_types + more_teas
print(all_teas) # ('black', 'green', 'herbal', 'oolong', 'white', 'chamomile', 'matcha', 'chai')
# Repeating tuples
repeated_teas = tea_types * 2
print(repeated_teas) # ('black', 'green', 'herbal', 'oolong', 'white', 'chamomile', 'black', 'green', 'herbal', 'oolong', 'white', 'chamomile')
# Nested tuples
nested_tuple = (tea_types, more_teas)
print(nested_tuple) # (('black', 'green', 'herbal', 'oolong', 'white', 'chamomile'), ('matcha', 'chai'))
# Unpacking tuples
first_tea, second_tea, *rest = tea_types 
print(first_tea)  # 'black'
print(second_tea)  # 'green'
print(rest)  # ['herbal', 'oolong', 'white', 'chamomile']
# Tuple with a single element
single_tea = ('matcha',)    
print(single_tea)  # ('matcha',)
print(type(single_tea))  # <class 'tuple'>
not_a_tuple = ('matcha')    
print(type(not_a_tuple))  # <class 'str'>
# Converting list to tuple
tea_list = ['black', 'green', 'herbal']
tea_tuple = tuple(tea_list)
print(tea_tuple)  # ('black', 'green', 'herbal')
# Converting tuple to list
new_tea_list = list(tea_tuple)
print(new_tea_list)  # ['black', 'green', 'herbal']
# Using tuples as dictionary keys   
tea_dict = {('black', 'green'): 'Popular teas'}
print(tea_dict)  # {('black', 'green'): 'Popular teas'}