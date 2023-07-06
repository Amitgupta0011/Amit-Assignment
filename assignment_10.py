### 1. Write a Python program to find sum of elements in list?
def calculate_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Example usage
my_list = [1, 2, 3, 4, 5]
result = calculate_sum(my_list)
print("Sum of elements:", result)

### 2. Write a Python program to  Multiply all numbers in the list?
def multiply_numbers(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Example usage
my_list = [1, 2, 3, 4, 5]
result = multiply_numbers(my_list)
print("Multiplication result:", result)


### 3. Write a Python program to find smallest number in a list?
def find_smallest(lst):
    if not lst:
        return None
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

# Example usage
my_list = [5, 2, 8, 1, 9]
result = find_smallest(my_list)
print("Smallest number:", result)


### 4. Write a Python program to find largest number in a list?
def find_largest(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

# Example usage
my_list = [5, 2, 8, 1, 9]
result = find_largest(my_list)
print("Largest number:", result)


### 5. Write a Python program to find second largest number in a list?
def find_second_largest(lst):
    if len(lst) < 2:
        return None
    largest = lst[0]
    second_largest = None
    for num in lst[1:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest:
            if second_largest is None or num > second_largest:
                second_largest = num
    return second_largest

# Example usage
my_list = [5, 2, 8, 1, 9]
result = find_second_largest(my_list)
print("Second largest number:", result)


### 6. Write a Python program to find N largest elements from a list?
def find_n_largest(lst, n):
    if n > len(lst):
        return None
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[:n]

# Example usage
my_list = [5, 2, 8, 1, 9, 3, 7, 6]
n = 3
result = find_n_largest(my_list, n)
print(f"{n} largest elements:", result)


### 7. Write a Python program to print even numbers in a list?
def print_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            print(num)

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:")
print_even_numbers(my_list)


### 8. Write a Python program to print odd numbers in a List?
def print_odd_numbers(lst):
    for num in lst:
        if num % 2 != 0:
            print(num)

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Odd numbers:")
print_odd_numbers(my_list)


### 9. Write a Python program to Remove empty List from List?
def remove_empty_lists(lst):
    return [sublist for sublist in lst if sublist]

# Example usage
my_list = [1, 2, [], 3, [], [4, 5], 6, [], 7, 8, []]
result = remove_empty_lists(my_list)
print("List with empty lists removed:", result)


### 10. Write a Python program to Cloning or Copying a list?
def clone_list(lst):
    return lst.copy()

# Example usage
my_list = [1, 2, 3, 4, 5]
cloned_list = clone_list(my_list)
print("Original list:", my_list)
print("Cloned list:", cloned_list)


### 11. Write a Python program to Count occurrences of an element in a list?
def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage
my_list = [1, 2, 3, 2, 4, 1, 2, 5]
element = 2
occurrences = count_occurrences(my_list, element)
print(f"Number of occurrences of {element}: {occurrences}")


