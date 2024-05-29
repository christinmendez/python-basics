#leapyear
year=int(input("enter the year :  "))
import calendar
if calendar.isleap(year):
    print("it is a leap year")
else:
    print("it is not a leap year")
#primenumber
number=int(input("enter a positive num : "))
if number == 1:
    print(number,"it is not a prime number")
elif number >1:
    for i in range(2,number):
        if (number%i)==0:
            print(i,"it is not a prime num")
            break
    else:
        print(i,"it is a prime num")
#circle surface area
from math import pi
x=float(input("enter the radius of the circle :  "))
area=pi*x**2
print(area)
#sphear surface area
radius=int(input("enter the radius :"))
area=4*pi*radius**2
print(area)
#area of a cone
def surfacearea(r,h):
    return pi*r*h+pi*r*r
radius=float(input("enter the radius : "))
height=float(input("enter the height : "))
print(surfacearea(radius,height))

