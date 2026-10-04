# 1-D Array (List) create kar rahe hain
arr = [5,10,20,25,30,35]

# Array print kar rahe hain
print("Array element:",arr)

# Index ke through elements access kar rahe hain
print("Index 0 par element:",arr[0])
print("Index 2 par element:",arr[2])
print("Index 5 par element:",arr[5])

# Loop chala kar saare index aur unke elements print kar rahe hain
for i in range(len(arr)):
    print(f"Index {i} -> Element {arr[i]}")

# Array element: [5, 10, 20, 25, 30, 35]
# Index 0 par element: 5
# Index 2 par element: 20
# Index 5 par element: 35
# Index 0 -> Element 5
# Index 1 -> Element 10
# Index 2 -> Element 20
# Index 3 -> Element 25
# Index 4 -> Element 30
# Index 5 -> Element 35