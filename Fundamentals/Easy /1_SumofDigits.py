# Using String Conversion

def sumOfDegit(n):

    # Convert number to string 
    s = str(n) # "687"
    total_sum = 0 

    # Number ko text (string) me badal kar har digit ko add karo

    for degit in s:
        total_sum = total_sum + int(degit) # "6","8","7" --> at a time are came :- > 6,8,7 

    print("Sum of degit:",total_sum)

sumOfDegit(687)

# Sum of degit: 21 
