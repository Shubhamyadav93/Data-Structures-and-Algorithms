li = [2,3,8,4,5,3]

# Maximum element 
max_ele = li[0]
for i in range(0,len(li)):
    if li[i] > max_ele:
        max_ele = li[i]
print(max_ele)

# Minimum element 
min_ele = li[0]
for i in range(0,len(li)):
    if li[i] < min_ele:
        min_ele = li[i]
print(min_ele)


# OR 

max_ele = li[0]
for ele in li:
    if max_ele < ele:
        max_ele = ele
print(max_ele)

min_ele = li[0]
for ele in li:
    if min_ele > ele:
        min_ele = ele
print(min_ele)


# Reversing a List 
li = [2, 3, 8, 4, 5, 3] 
# li.reverse()
# print(li) 

n = len(li)
rev_li = []
for i in range(n-1,-1,-1):
    rev_li.append(li[i])
print(rev_li)




