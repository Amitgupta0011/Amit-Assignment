### 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 10

if n_terms <= 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
for i in range(n_terms):
	print(recursive_fibonacci(i))



### 2. Write a Python Program to Find Factorial of Number Using Recursion?
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a non-negative integer: "))
result = factorial(number)
print("The factorial of", number, "is", result)



### 3. Write a Python Program to calculate your Body Mass Index?
def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print("Your Body Mass Index (BMI) is:", round(bmi, 2))



### 4. Write a Python Program to calculate the natural logarithm of any number?
import math

number = float(input("Enter a positive number: "))

if number > 0:
    result = math.log(number)
    print("The natural logarithm of", number, "is", result)
else:
    print("Error: Please enter a positive number.")



### 5. Write a Python Program for cube sum of first n natural numbers?
def cube_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 3
    return sum

n = int(input("Enter a positive integer: "))
result = cube_sum(n)
print("The cube sum of the first", n, "natural numbers is", result)






