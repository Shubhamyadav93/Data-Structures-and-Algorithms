# 2D Array (Matrix - 3 rows and 3 columns) create kar rahe hain

arr_2d = [
    [1,2,3], # Row 0 
    [4,5,6], # Row 1 
    [7,8,9] # Row 2 
]

# Element access kar rahe hain arr_2d[row][col]
print("Row 0, col 1 par element:",arr_2d[0][1]) # Output: 2
print("Row 2. col 0 par element:", arr_2d[2][0])# Output: 7 

# # Table (Grid) ke format mein print karne ke liye:

for row in range(len(arr_2d)):
    for col in range(len(arr_2d[row])):
        print(arr_2d[row][col],end=" ")

    print()


# Row 0, col 1 par element: 2
# Row 2. col 0 par element: 7
# 1 2 3 
# 4 5 6 
# 7 8 9 


