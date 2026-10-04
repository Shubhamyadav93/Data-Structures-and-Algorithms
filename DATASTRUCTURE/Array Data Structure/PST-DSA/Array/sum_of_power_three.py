def sum_of_power_three(n):
    x = 1 
    sum = 0 
    while 3**x <= n:
        if sum + 3 ** x  == n :
            print(sum)
            # return True

        x = x + 1 

    # print("False")
    # return False 

print(sum_of_power_three(9))

