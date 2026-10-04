#  Python program to insert a given element at the beginning 

arr = [10,20,30,40]
element = 50 
print("Array before insertion")
for i in range(len(arr)):
    print(arr[i])

# Insert element at the beginning 
arr.insert(0,50)

print("\nArray after insetion")
for i in range(len(arr)):
    print(arr[i],end=" ")


# Array before insertion
# 10 20 30 40 
# Array after insertion
# 50 10 20 30 40 

# ------------------------------------------------------------------------------------v------ 

# [Approach 2] Using Custom Method

arr = [10,20,30,40,0]
n = 4 
element = 50 
print("Array before insertion")
for i in range(n):
    print(arr[i],end=" ")

print("Array before insertion")
# Shift all element to the right 
for i in range(n-1,-1,-1):
    arr[i+1] = arr[i] 


# Insert new element at beginning 
arr[0] = element 
print("\nArray element insertion")
for i in range(n+1):
    print(arr[i],end=" ")

# 10 20 30 40 
# Array element insertion
# 50 10 20 30 40     



