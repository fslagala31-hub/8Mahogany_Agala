import math

#Ask the user to enter the coordinates of the first point
x1 = float(input ("Enter x1: "))
y1 = float(input ("Enter y1: "))

#Ask the user to enter the coordinates for the second point 
x2 = float(input ("Enter x2: "))
y2 = float(input ("Enter y2: "))

#Compute the distance using the distance formula
distance = math.sqrt (math.pow (x2 - x1, 2) + math.pow (y2 - y1, 2))

#It will display the results rounded to to two decimal places
print("The distance btween the two points is:",round(distance, 2))



#Reflection
# Using the math library made things easier and more practical because it provided readymade functions like sqrt() and pow(), making the calculations more reliable. Without them i would have to write a
# longer and more complicated code.