### 1. Write a Python program to check if the given number is a Disarium Number?
def is_disarium(number):
    num_str = str(number)
    n = len(num_str)
    sum = 0
    
    for i in range(n):
        digit = int(num_str[i])
        sum += digit ** (i + 1)
    
    if sum == number:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_disarium(num):
    print(num, "is a Disarium number")
else:
    print(num, "is not a Disarium number")


### 3. Write a Python program to check if the given number is Happy Number?
def is_happy_number(number):
    def calculate_square_sum(n):
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit ** 2
            n //= 10
        return sum
    
    slow = fast = number
    while True:
        slow = calculate_square_sum(slow)
        fast = calculate_square_sum(calculate_square_sum(fast))
        if slow == fast:
            break
    
    return slow == 1

num = int(input("Enter a number: "))
if is_happy_number(num):
    print(num, "is a Happy number")
else:
    print(num, "is not a Happy number")



### 4. Write a Python program to print all happy numbers between 1 and 100?
def is_happy_number(number):
    def calculate_square_sum(n):
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit ** 2
            n //= 10
        return sum
    
    slow = fast = number
    while True:
        slow = calculate_square_sum(slow)
        fast = calculate_square_sum(calculate_square_sum(fast))
        if slow == fast:
            break
    
    return slow == 1

print("Happy numbers between 1 and 100:")
for num in range(1, 101):
    if is_happy_number(num):
        print(num)



### 5. Write a Python program to determine whether the given number is a Harshad Number?
def is_harshad_number(number):
    digit_sum = sum(int(digit) for digit in str(number))
    
    if number % digit_sum == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_harshad_number(num):
    print(num, "is a Harshad number")
else:
    print(num, "is not a Harshad number")


### 6. Write a Python program to print all pronic numbers between 1 and 100?
def is_pronic_number(number):
    for i in range(1, int(number**0.5) + 1):
        if i * (i + 1) == number:
            return True
    return False

print("Pronic numbers between 1 and 100:")
for num in range(1, 101):
    if is_pronic_number(num):
        print(num)

