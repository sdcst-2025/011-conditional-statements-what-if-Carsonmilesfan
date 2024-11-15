#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
x = float(input("what is side one? "))
y = float(input("what is side two? "))
z = float(input("what is side three? "))

if x > y and x:
    n = x
elif y > x and z:
    n = y
elif z > x and y:
    n = z
else:
    n = x

if n**2 == x**2 + y**2 + z**2 - n**2:
    print("this is not an obtuse triangle")
    print("this is not an acute triangle")
    print("this is a right triangle")
elif n**2 > x**2 + y**2 + z**2 - n**2:
    print("this is not an acute triangle")
    print("this is not a right triangle")
    print("this is an obtuse triangle")
elif n**2 < x**2 + y**2 + z**2 - n**2:
    print("this is not a right triangle")
    print("this is not an obtuse triangle")
    print("this is an acute triangle")
else:
    print("this is not an obtuse triangle")
    print("this is not an acute triangle")
    print("this is not a right triangle")
