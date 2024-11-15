#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""

x = int(input("number "))

if x > 0:
    print("positive")
elif x < 0:
    print("negative")
elif x == 0:
    print("zero")
