### 1. Write a Python program to print "Hello Python"?
print("Hello Python")

### 2. Write a Python program to do arithmetical operations addition and division.?
a=int(input("type 1st number"))
b=int(input("type 2st number"))

print("the sum of two numer is:- ", a+b)
print("the division of two number is: ",a/b)

### 3. Write a Python program to find the area of a triangle?
a = int(input("Enter the base length of the triangle: "))
b = int(input("Enter the height of the triangle: "))
c = 0.5 * a * b
print("The area of the triangle is:", c)

### 4. Write a Python program to swap two variables?
a=input("type 1st variable :-")
print("a=",a)
b=input("type 2nd variable:- ")
print("b=",b)

a,b=b,a

print("after swaping")
print("a=",a)
print("b=",b)

### 5. Write a Python program to generate a random number?
import random
a=random.randint(1,50)
print(a)
