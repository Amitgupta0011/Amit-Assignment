
### 1. Write a program that calculates and prints the value according to the given formula:
import math

C = 50
H = 30

def calculate_values(input_sequence):
    values = input_sequence.split(',')
    results = []
    for value in values:
        D = int(value)
        Q = math.sqrt((2 * C * D) / H)
        results.append(str(round(Q)))
    return ','.join(results)

# Example usage
input_sequence = "100,150,180"
output = calculate_values(input_sequence)
print(output)


### 2. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
def generate_2d_array(X, Y):
    array = [[0 for j in range(Y)] for i in range(X)]
    for i in range(X):
        for j in range(Y):
            array[i][j] = i * j
    return array

# Example usage
X = int(input("Enter the number of rows (X): "))
Y = int(input("Enter the number of columns (Y): "))

result_array = generate_2d_array(X, Y)

# Print the resulting 2D array
for row in result_array:
    print(row)

### 3. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
def sort_words(input_sequence):
    words = input_sequence.split(',')
    sorted_words = sorted(words)
    return ','.join(sorted_words)

# Example usage
input_sequence = input("Enter a comma-separated sequence of words: ")
sorted_sequence = sort_words(input_sequence)
print(sorted_sequence)


### 4. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
def remove_duplicates_and_sort(input_sequence):
    words = input_sequence.split()
    unique_words = list(set(words))
    sorted_words = sorted(unique_words)
    return ' '.join(sorted_words)

# Example usage
input_sequence = input("Enter a sequence of whitespace-separated words: ")
processed_sequence = remove_duplicates_and_sort(input_sequence)
print(processed_sequence)


### 5. Write a program that accepts a sentence and calculate the number of letters and digits.
def count_letters_and_digits(sentence):
    letters = 0
    digits = 0
    for char in sentence:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return letters, digits

# Example usage
sentence = input("Enter a sentence: ")
letter_count, digit_count = count_letters_and_digits(sentence)
print("Number of letters:", letter_count)
print("Number of digits:", digit_count)


### 6. A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
def is_valid_password(password):
    if len(password) < 8:
        return False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
    return has_uppercase and has_lowercase and has_digit

# Example usage
password = input("Enter a password: ")
validity = is_valid_password(password)
if validity:
    print("Password is valid.")
else:
    print("Password is invalid.")

