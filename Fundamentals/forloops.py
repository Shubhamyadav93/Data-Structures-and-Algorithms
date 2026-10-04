for i in range(1,6):
    print(i,end=" ")
print()

# 1. Basic For Loop
for i in range(2,11,2):
    print(i,end=" ")
print()

# 2. For Each Loop

number = [1,2,3,4,5]
for num in number:
    print(num,end=" ")

# 3. For Loop with Multiple Variables

i , j = 0 , 10
while(i<5 and j>0):
    print("i=",i,"j=",j)
    i+=1
    j-=1

# 4. Infinite For Loop

# 5. Nested For Loop

for i in range(1,4):
    for j in range(1,4):
        print(i*j,end=" ")
    print()

# 6. For Loop with Step/Stride

for i in range(0,10,2):
    print(i,end=" ")

print()



# _________________________________________________________________________________________________________________________________________________________________________________________________________________

# Write a program to print table of a number 

for i in range(1,11):
    print(i*3)
print()


for i in range(1,11):
    print(i*5)


n = int(input("Enter the number :"))
for i in range(n+1):
    print(i*n)

