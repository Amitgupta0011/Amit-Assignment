### 1. Write a Python program to find words which are greater than given length k?
def find_words_greater_than_length(word_list, k):
    result = []
    for word in word_list:
        if len(word) > k:
            result.append(word)
    return result

# Example usage
my_list = ["apple", "banana", "orange", "kiwi", "grapefruit"]
length = 5
words_greater_than_length = find_words_greater_than_length(my_list, length)
print(f"Words greater than length {length}: {words_greater_than_length}")

### 2. Write a Python program for removing i-th character from a string?
def remove_character(string, i):
    if i < 0 or i >= len(string):
        return string
    return string[:i] + string[i+1:]

# Example usage
my_string = "Hello, World!"
index = 7
modified_string = remove_character(my_string, index)
print("Modified string:", modified_string)


### 3. Write a Python program to split and join a string?
def split_and_join(string):
    # Splitting the string into a list of words
    words = string.split()

    # Joining the list of words into a string using a space as the separator
    joined_string = ' '.join(words)

    return joined_string

# Example usage
my_string = "Hello, this is a sample string"
split_and_joined_string = split_and_join(my_string)
print("Split and joined string:", split_and_joined_string)


### 4. Write a Python to check if a given string is binary string or not?
def is_binary_string(string):
    for char in string:
        if char != '0' and char != '1':
            return False
    return True

# Example usage
my_string = "101010"
is_binary = is_binary_string(my_string)
if is_binary:
    print("The string is a binary string.")
else:
    print("The string is not a binary string.")


### 5. Write a Python program to find uncommon words from two Strings?
def find_uncommon_words(string1, string2):
    words1 = set(string1.split())
    words2 = set(string2.split())
    
    uncommon_words = words1.symmetric_difference(words2)
    
    return uncommon_words

# Example usage
string1 = "Hello world this is a string"
string2 = "Hello Python this is another string"
uncommon_words = find_uncommon_words(string1, string2)
print("Uncommon words:", uncommon_words)


### 6. Write a Python to find all duplicate characters in string?
def find_duplicate_characters(string):
    duplicates = []
    char_count = {}
    
    for char in string:
        if char in char_count:
            char_count[char] += 1
            if char not in duplicates:
                duplicates.append(char)
        else:
            char_count[char] = 1
    
    return duplicates

# Example usage
my_string = "Hello, World!"
duplicate_chars = find_duplicate_characters(my_string)
print("Duplicate characters:", duplicate_chars)


### 7. Write a Python Program to check if a string contains any special character?
def contains_special_character(string):
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    for char in string:
        if char in special_characters:
            return True
    return False

# Example usage
my_string = "Hello, World!"
contains_special_char = contains_special_character(my_string)
if contains_special_char:
    print("The string contains special characters.")
else:
    print("The string does not contain special characters.")
