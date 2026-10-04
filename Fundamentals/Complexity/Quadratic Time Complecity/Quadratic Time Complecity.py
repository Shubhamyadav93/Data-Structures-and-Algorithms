# Concept A: Standard Nested Loops (Loop ke andar Loop)
def print_all_pair(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i],arr[j])

# print_all_pair([2,5,8,3,7,4])

# Concept B: Triangular Nested Loops (Half Loops)

def print_unique_pairs(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            print(arr[i],arr[j])

# print_unique_pairs([2,3,4,5])

# Concept C: Do Alag Inputs (O(N * M) vs O(N^2))

def compare_list(list1,list2):
    for item1 in list1:
        for item2 in list2:
            print(item1,item2)

compare_list([2,3,4,2,4],[9,4,2,4,3,5]) # O(N * M) --> Complexity ye hoga kyu ki dono list ke size same nahi hai 
compare_list([3,4,2,1],[3,1,4,2]) # O(N^2) --> Complexity hoga kyu ki yaha pe dono list ka size same hai thats wise 

