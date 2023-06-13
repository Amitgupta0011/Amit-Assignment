### 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
num=int(input("enter a number"))

if num>0:
    print("positive")
elif num==0:
    print("number is zero")
else:
    print("negative")
    
    
    
### 2. Write a Python Program to Check if a Number is Odd or Even?
num=int(input("enter a number"))
if num%2==0:
    print("even number")
else:
    print("odd number")
    
    

### 3. Write a Python Program to Check Leap Year?
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

year_input = int(input("Enter a year: "))
if is_leap_year(year_input):
    print(year_input, "is a leap year.")
else:
    print(year_input, "is not a leap year.")
    
    
    
### 4. Write a Python Program to Check Prime Number?
number = int(input("Enter a number: "))

# Prime numbers are greater than 1
if number > 1:
    # Check for factors
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            print("The number is not a prime number.")
            break
    else:
        print("The number is a prime number.")
else:
    print("The number is not a prime number.")
    
    

### 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

for i in range (1,10001):
    if i>1:
        for number in range(2,int(i/2)+1):
            if i%number==0:
                break
        else :
            print(i)
    

