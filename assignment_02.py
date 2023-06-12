###1. Write a Python program to convert kilometers to miles?
KM= float(input("enter Distance in kM:-"))
miles= KM*0.621371
print("Distance in miles is ", miles)


### 2.Write a Python program to convert Celsius to Fahrenheit?
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)


###3. Write a Python program to display calendar?
import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

cal = calendar.monthcalendar(year, month)

print(calendar.month_name[month], year)
print("Mo Tu We Th Fr Sa Su")
for week in cal:
    for day in week:
        if day == 0:
            print("  ", end=" ")
        else:
            print(f"{day:2d}", end=" ")
    print()


### 4. Write a Python program to solve quadratic equation?
a= float(input("type a"))
b=float(input("type b"))
c=float(input("type c"))

if b**2 - 4*a*c > 0:
    root1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    root2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    print(root1, root2)
    
elif (b**2 - 4*a*c)== 0:
    root = -b / (2*a)
    print(root)

else:
    print("No real roots")


###5. Write a Python program to swap two variables without temp variable?
a=input("type 1st variable :-")
print("a=",a)
b=input("type 2nd variable:- ")
print("b=",b)

a,b=b,a

print("after swaping")
print("a=",a)
print("b=",b)
