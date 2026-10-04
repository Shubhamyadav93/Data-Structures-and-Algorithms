def sum_of_square(n):
    sum = 0 
    for i in range(1,n+1):
        sqr = i ** 2 
        sum = sum + sqr 
    print(sum)

n = 3
sum_of_square(n)

# Method 2 
# [Expected Approach]- Using Mathematical Formulae - O(1) Time and O(1) Space

def sum_of_square_natural_number(n):
    return (n * (n+1) * (2 * n + 1)) / 6 

n = 5
print(sum_of_square_natural_number(n))

