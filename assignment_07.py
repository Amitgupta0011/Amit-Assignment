### 1. Write a Python Program to find sum of array?
array= [45,23,7,43,65,35,9,4,57,36,54]

sum=0
for i in array:
    sum=sum+i
print(sum)


### 2. Write a Python Program to find largest element in an array?
array= [45,23,7,43,65,35,9,4,57,36,103]

num=0
for i in array:
    if i>num:
        num=i
    else:
        num
        
print(num)

### 3. Write a Python Program for array rotation?
def rotate_array(arr, k):
    n = len(arr)
    k = k % n

    rotated_arr = arr[k:] + arr[:k]
    return rotated_arr

my_array = [1, 2, 3, 4, 5]
rotation_amount = 2
result = rotate_array(my_array, rotation_amount)
print("Original array:", my_array)
print("Rotated array:", result)


### 4. Write a Python Program to Split the array and add the first part to the end?
def split_and_add(arr, k):
    n = len(arr)
    k = k % n

    split_arr = arr[k:] + arr[:k]
    return split_arr

array = [1, 2, 3, 4, 5]
split_position = 2
result = split_and_add(array, split_position)
print("Original array:", array)
print("Split and added array:", result)


### 5. Write a Python Program to check if given array is Monotonic?
def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            increasing = False
        if arr[i] > arr[i - 1]:
            decreasing = False

    return increasing or decreasing

my_array = [1, 2, 3, 4, 5]
result = is_monotonic(my_array)
print("Is the array monotonic?", result)





