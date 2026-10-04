# Pattern 1: Loop Variable Divide ($/=$) ya Multiply ($*=$) ho raha ho

# Devision Loop --> O(log N)
def log_div(n):
    while n > 1:
        print(n)
        n = n //2 # Har step par input aadha ho raha hai
        
log_div(10)

#  Multiplication Loop --> O(log N)
def log_mult(n):
    i = 1 
    while i < n:
        print(i) 
        i = i * 2 

log_mult(50) # 1, 2, 4, 8, 16, 32... N tak pahunchne mein log N steps lega

# Pattern 2: Binary Search (The Gold Standard of O(log N))

# Sorted array mein search karne ka sabse famous algorithm:
def binary_search(arr,target):
    low = 0 
    high = len(arr) -1 

    while low <= high:
        mid = (low + high)

        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1 # Left half discard
        else:
            high = mid - 1 # Right half discard
    
    return -1 

print(binary_search([2,3,5,6,8],6)) 


