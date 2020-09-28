#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
import math
a = float(input("Give me one side of a triangle\n"))
b = float(input("Give me another side of a triangle\n"))
c = float(input("Give me another side of a triangle\n"))

if a > b and a > c:
    c=a
if b > a and b > c:
    c=b
if c > a and c > b:
    s = 100*(math.sqrt(a**2 + b**2))/c

if int(s) in range (98,102) :
    print("that is a right triangle")


