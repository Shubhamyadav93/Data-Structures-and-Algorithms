# x = 0 
# n = 1 
# if n == pow(2,exp=x): 
#     print(True)
# print(False)

# def power_two(n):
#     x = 0 
#     if n == 2 ** x:
#         return True
#     x = x + 1
#     return False 
# print(power_two(2))   # ---> This is my first leetcode , here I am one mistake I am not used here loop thats way 


#  This is incorrect code 

def power_of_two(n):
    x = 0 
    while x <= n : 
        if n== 2 ** x :
            return True 
        x = x + 1 
    return False  
print(power_of_two(2))  # --> ye bhi galat hai out ishme to aaya leki baad me bhi idar jab n--> bada hoga to TLE aayega 



# ------------------------------------------------------------------------------------------------------------------------------
# Correct code 
def power_of_two(n):

    # Edge Case 
    if n <= 0: 
        return False 
    x = 0 
    while 2 ** x <= n : 
        if 2 ** x == n :
            return True

        x = x + 1 
    return False 

print(power_of_two(10))

# ------------------------------------------------------------------------------------------------------------------------------------------------

