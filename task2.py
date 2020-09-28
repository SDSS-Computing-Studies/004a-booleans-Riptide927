#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"

a = int(input("Give me a number\n"))
if a < 0:
    print("your number is negative")
elif a > 0:
    print("your number is positive")
elif a ==0:
    print("your number is zero")