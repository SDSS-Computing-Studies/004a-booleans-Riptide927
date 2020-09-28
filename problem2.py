#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

a = float(input("Input a number \n"))

if a % 1 == 0:
    print("the number is an integer")
else:
    print("the number is not an integer")
