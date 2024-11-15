#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# There are many ways to solve this problem
# Hint: One method is to use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"

x = float(input("a number "))
y = 0.5 * x
n = int(y)

if n == y:
    print("the number is even")
else:
    print ("the number is odd")
