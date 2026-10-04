# If Condition 
x = 7 
if(x > 0):
    print("x is positive")


# If-else Condition 

x = -5 
if(x > 0):
    print("x is positive")
else:
    print("x is not positive")


# If-else if Condition statement 

x = 0 
if(x > 0):
    print("x is positive")
elif(x < 0):
    print("x is negative")
else:
    print("x is zero")


# Switch Statement 

day = 2 

match day: 
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")

    case _:
        print("Invalid day!")



# Key Considerations for Switch Case Statements
# 1) Constant Expression 

x = 10 
y = 5 

match x + y :
    case 15:
        print("Result is 15")

    case 20:
        print("Result is 20")
    
    case _:
        print("No match found")


# 2) Limited to certain type 
grade = "B"

match grade:
    case 'A':
        print("Excellent")

    case 'B':
        print("Good!")
    
    case _:
        print("Not specified.")

# 3) Ternary Expression Conditional Statement 
x = 10 
print("x is positive" if x > 0 else "x is not positive")


# Nested Ternary Operator 
x = 0 
print("x is positive" if x > 0 else(
    "x is not positive" if x < 0 else "x is zero"
))



# __________________________________________________________________________________________________________________________________________________________________________________________________________________


# Even - Odd

"""
x = int(input("Enter the number to the users:"))

if(x%2==0):
    print("Yes it is a evan number")

else:
    print("Not it is not a evan number it is a odd number")

"""
# Positive, Negative, Zero 
"""
n = int(input("Enter the integer number:"))
if(n > 0):
    print("It is a positive number")
elif(n<0):
    print("IT is a negative number.")
else:
    print("It is a zero")
"""

# Decide if an input number is 
# a) Positive Evan 
# b) Positive Odd 
# c) Negative Evan 
# d) Negative Odd 
# e) Zero 

"""
n = int(input("Enter the number from the users"))

if(x%2==0 and x > 0):
    print("Positive Even number")
elif(x%2==0 or x > 0):
    print("Positive odd")
elif(x%2==0 and x < 0):
    print("Negative Even")
elif(x%2==0 or x < 0):
    print("Negative odd")
else:
    print("Zero")

# These code are only print Positive and zero but your code are writien negative part 
"""


"""

n = int(input("Enter the number:"))

if(n>0):
    print("Positive",end=" ")
    if(n%2==0):
        print(" even")
    else:
        print(" odd")
elif(n<0):
    print("Negative", end=" ")
    if(n%2==0):
        print("even")
    else:
        print("odd")
else:
    print("zero")

"""


a = int(input("Enter the number of a :"))
b = int(input("Enter the number of b :" ))

if(a>b):
    print("a is greater than b:",a)
elif(b>a):
    print("b is greater than a:",b)
else:
    print(f"a and b is same:{a},{b}") 



