arr = [10,20,30,40]
pos = 2 
ele = 50 
n = len(arr)
# for i in range(n):
#     arr[2] = ele
# print(arr) # [10, 20, 50, 40] <- Here it is replace the element in arraay 

# ----------------------
for i in range(n):
    arr.insert(2,50)
print(arr)#[10, 20, 50, 50, 50, 50, 30, 40] <- These different answer are came , but these question are not proper way 

# ------------ # # ------------ # # ------------ # # ------------ # # ------------ # # ------------ # # ------------ # # ------------ # # ------------ # 

# But my Question is you dont replace the arry element, you have put the element in array , you have move the element .



                                                        # ============================================ #
                                                            # [Approach 1] Using Built-In Methods  # 
                                                        # ============================================ # 


arr = [100,200,300,400,500]
posision = 2 
element = 600
arr.insert(posision-1,element)
# Printing ways 
print(arr)#[100, 600, 200, 300, 400, 500]
#  Or 
for i in arr:
    print(i,end=" ")#100 600 200 300 400 500 

# OR 
for i in range(len(arr)):
    print(arr[i],end=" ")#100 600 200 300 400 500 



# ________________________________________________________________________________________________________________________________________________________________________________
                                                       

                                                    #    ============================================================    #
                                                                # [Approach 2] Using Custom Method # 
                                                    #    ============================================================    #


arr = [10,20,30,40,0]
n = 4 
ele = 50 
pos = 2 

for i in range(n,pos-1,-1):
    arr[i] = arr[i-1]

arr[pos-1] = ele 

print(arr) #  [10, 50, 20, 30, 40] 














