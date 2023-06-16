### 1. Write a Python Program to Find the Factorial of a Number?
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


max_num = max(num1, num2)
lcm = max_num

while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += max_num
print("The LCM of", num1, "and", num2, "is",lcm)


### 2. Write a Python Program to Find HCF?
def find_hcf(num1, num2):
    
    min_num = min(num1, num2)

    hcf = 1  

    
    for i in range(1, min_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i

    return hcf

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


hcf = find_hcf(num1, num2)

print("The HCF of", num1, "and", num2, "is", hcf)


### 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
num= int(input("enter a number: "))

print("binary", bin(num)[2:])
print("octal",oct(num)[2:])
print("hexadecimal", hex(num)[2:])

### 4. Write a Python Program To Find ASCII value of a character?
character = input("Enter a character: ")

ascii_value = ord(character)

print("The ASCII value of", character, "is", ascii_value)


### 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice (1-4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))

        break
    else:
        print("Invalid input. Please enter a valid choice (1-4).")


