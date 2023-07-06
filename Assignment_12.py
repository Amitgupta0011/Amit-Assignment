### 1. Write a Python program to Extract Unique values dictionary values?
def extract_unique_values(dictionary):
    unique_values = set()
    for values in dictionary.values():
        unique_values.update(values)
    return list(unique_values)

# Example usage
my_dict = {
    'key1': [1, 2, 3],
    'key2': [2, 3, 4],
    'key3': [3, 4, 5]
}
unique_values = extract_unique_values(my_dict)
print("Unique values:", unique_values)

### 2. Write a Python program to find the sum of all items in a dictionary?
def sum_of_items(dictionary):
    total_sum = 0
    for value in dictionary.values():
        total_sum += sum(value)
    return total_sum

# Example usage
my_dict = {
    'key1': [1, 2, 3],
    'key2': [4, 5, 6],
    'key3': [7, 8, 9]
}
result = sum_of_items(my_dict)
print("Sum of all items:", result)


### 3. Write a Python program to Merging two Dictionaries?
def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dictionary = merge_dictionaries(dict1, dict2)
print("Merged dictionary:", merged_dictionary)


### 4. Write a Python program to convert key-values list to flat dictionary?
def convert_to_flat_dictionary(key_value_list):
    flat_dict = {}
    for pair in key_value_list:
        key = pair[0]
        value = pair[1]
        flat_dict[key] = value
    return flat_dict

# Example usage
key_value_list = [('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]
flat_dictionary = convert_to_flat_dictionary(key_value_list)
print("Flat dictionary:", flat_dictionary)


### 5. Write a Python program to insertion at the beginning in OrderedDict?
from collections import OrderedDict

def insert_at_beginning(odict, key, value):
    odict.pop(key, None)  # Remove the key if already present
    odict.move_to_end(key, last=False)  # Move the key to the beginning
    odict[key] = value  # Insert the key-value pair at the beginning

# Example usage
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print("Original OrderedDict:", ordered_dict)

insert_at_beginning(ordered_dict, 'd', 4)
print("After insertion at the beginning:", ordered_dict)


### 6. Write a Python program to check order of character in string using OrderedDict()?
from collections import OrderedDict

def check_order_of_characters(string):
    ordered_dict = OrderedDict()
    for char in string:
        ordered_dict[char] = None

    ordered_string = ''.join(ordered_dict.keys())
    if ordered_string == string:
        return True
    else:
        return False

# Example usage
my_string = "hello world"
is_ordered = check_order_of_characters(my_string)
if is_ordered:
    print("The order of characters is maintained.")
else:
    print("The order of characters is not maintained.")


### 7. Write a Python program to sort Python Dictionaries by Key or Value?
def sort_dictionary(dictionary, by_key=True):
    sorted_dict = {}
    if by_key:
        sorted_keys = sorted(dictionary.keys())
        for key in sorted_keys:
            sorted_dict[key] = dictionary[key]
    else:
        sorted_items = sorted(dictionary.items(), key=lambda x: x[1])
        for item in sorted_items:
            sorted_dict[item[0]] = item[1]
    return sorted_dict

# Example usage
my_dict = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
sorted_by_key = sort_dictionary(my_dict, by_key=True)
print("Sorted by Key:", sorted_by_key)

sorted_by_value = sort_dictionary(my_dict, by_key=False)
print("Sorted by Value:", sorted_by_value)





