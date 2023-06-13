# ### 1. Write a Python Program to Find the Factorial of a Number?
# number=int(input("enter a number: "))
# a=1
# for i in range(1,number+1):
#     a=a*i
#     if i==number:
#         print(a)
        
        

# ### 2. Write a Python Program to Display the multiplication Table?
# number= int(input("enter a number"))
# for i in range(1,11):
#     print(number,"x",i,"=",number*i)
    
    

# ### 3. Write a Python Program to Print the Fibonacci sequence?
# terms = int(input("Enter the number of terms: "))

# # First two terms of the Fibonacci sequence
# first_term = 0
# second_term = 1

# # Print the first two terms
# print("Fibonacci sequence:")
# print(first_term)
# print(second_term)

# # Generate the remaining terms
# for i in range(2, terms):
#     next_term = first_term + second_term
#     print(next_term)
#     # Update the values of the previous two terms
#     first_term = second_term
#     second_term = next_term
    
    
# ### 5. Write a Python Program to Find Armstrong Number in an Interval?
# number = int(input("Enter a number: "))

# # Convert the number to a string to calculate the number of digits
# num_str = str(number)

# # Calculate the number of digits
# num_digits = len(num_str)

# # Initialize the sum
# armstrong_sum = 0

# # Calculate the sum of the cubes of each digit
# for digit in num_str:
#     armstrong_sum += int(digit) ** num_digits

# # Check if the number is an Armstrong number
# if number == armstrong_sum:
#     print(number, "is an Armstrong number.")
# else:
#     print(number, "is not an Armstrong number.")
    
    

### 6. Write a Python Program to Find the Sum of Natural Numbers?
n= int(input("enter a number"))

sum_of_numbers = (n * (n + 1)) // 2
print("The sum of natural numbers up to", n, "is", sum_of_numbers)
