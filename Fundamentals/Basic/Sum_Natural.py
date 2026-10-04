# Sum of Natural number 

def sumnatural(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i 
    print(sum)

n = 3
sumnatural(n)


# Recursion Method 

def sumnatural(n):
    if(n==0):
        return 0
    
    return n + sumnatural(n-1)

n = 5
print(sumnatural(n))

# Formula based method 

def sumnaturals(n):
    return n*(n+1)//2

n = 10 
print(sumnatural(n))




