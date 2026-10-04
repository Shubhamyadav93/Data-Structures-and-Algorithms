# # Array aur target value define kar rahe hain

arr = [10,25,30,45,50] 
target = 30
found = False

# Linear traversal ke zariye search kar rahe hain

for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element {target} index {i} par mil gaya!")
        found = True 
        break 


if not found:
    print(f"Element {target} array main nahi hai.")


# ==========================================================================================

