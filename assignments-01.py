import sys;
import datetime;
from math import pi;

# No. 1: Write a Python program to print the following string in a specific format
#Start

stringToPrint = """Twinkle, twinkle, little star,
\t How I wonder what you are!
\t\t Up above the world so high,
\t\t Like a diamond in the sky.
Twinkle, twinkle, little star,
\t How I wonder what you are"""

print (stringToPrint);

#End

# No. 2: Write a Python program to get the Python version you are using
#Start

print(sys.version);

#End


# No. 3: Write a Python program to display the current date and time.
#Start

currentDateAndTime = datetime.datetime.now();
print(currentDateAndTime); 

#End

# No. 4: Write a Python program which accepts the radius of a circle from the user
# and compute the area.
#Start

radius = float(input("Insert the radius of the circle : "));
calculateTheArea = pi*radius**2;

print("The area of circle with radius " + str(radius) + " is :" + str(calculateTheArea));

#End


# No. 5: Write a Python program which accepts the user's first and last name and
# print them in reverse order with a space between them.
#Start

firstName = str(input("Enter your first name"));
lastName = str(input("Enter your last name"));

print(lastName+" "+firstName);

#End


# No. 6: Write a python program which takes two inputs from user and print them
# addition
#Start

value1 = float(input("Enter first value"));
value2 = float(input("Enter second value"));

print(value1+value2);

#End