### 1. Write a Python Program to Add Two Matrices?
def add_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if rows1 != rows2 or cols1 != cols2:
        return None

    result = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

result = add_matrices(matrix1, matrix2)
if result is None:
    print("Matrix dimensions mismatch!")
else:
    print("Matrix 1:")
    for row in matrix1:
        print(row)
    print("Matrix 2:")
    for row in matrix2:
        print(row)
    print("Sum of matrices:")
    for row in result:
        print(row)



### 2. Write a Python Program to Multiply Two Matrices?
def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        return None

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Example usage
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

result = multiply_matrices(matrix1, matrix2)
if result is None:
    print("Matrix dimensions mismatch!")
else:
    print("Matrix 1:")
    for row in matrix1:
        print(row)
    print("Matrix 2:")
    for row in matrix2:
        print(row)
    print("Product of matrices:")
    for row in result:
        print(row)



### 3. Write a Python Program to Transpose a Matrix?
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed_matrix = transpose_matrix(matrix)

print("Original matrix:")
for row in matrix:
    print(row)

print("Transposed matrix:")
for row in transposed_matrix:
    print(row)




### 4. Write a Python Program to Sort Words in Alphabetic Order?
def sort_words(words):
    sorted_words = sorted(words)
    return sorted_words

word_list = ['banana', 'apple', 'cherry', 'date', 'grape']

sorted_words = sort_words(word_list)

print("Original word list:", word_list)
print("Sorted words:", sorted_words)


### 5. Write a Python Program to Remove Punctuation From a String?
import string

def remove_punctuation(text):
    no_punct = ""
    for char in text:
        if char not in string.punctuation:
            no_punct += char
    return no_punct

input_string = "Hello! How are you doing? I'm doing well."
result = remove_punctuation(input_string)
print("Input string:", input_string)
print("String without punctuation:", result)




