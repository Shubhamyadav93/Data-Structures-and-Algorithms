                                        # Insert Element at the End of an Array # 

# arr = [10,20,30,40]
# ele = 50 
# print("Print before insertion")
# for i in range(len(arr)):
#     print(arr[i])

# # Insert element at the element 
# arr.append(ele)

# print("\nArray after insertion")
# for i in range(len(arr)):
#     print(arr[i])


# Print before insertion
# 10
# 20
# 30
# 40

# Array after insertion
# 10
# 20
# 30
# 40
# 50


                                        # [Approach 2] Using Custom Method

n = 4 
arr = [10,20,30,40,0]
ele = 50 
print("Array before insertion")
for i in range(n):
    print(arr[i],end=" ")

# Inserting element at the end of the array 
arr[n] = ele 
print("\nArray after insertion")
for i in range(n+1):
    print(arr[i],end=" ")


# Array before insertion
# 10 20 30 40 
# Array after insertion
# 10 20 30 40 50

