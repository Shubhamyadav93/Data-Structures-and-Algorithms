# Using Third Variable 
a = 10 
b = 20 

temp = a 
a = b 
b = temp 
print("a :",a, "b :",b) 

# Using Arithmetic operation 
x = 10 
y = 20 

#swap two numbers using arithmetic operators
x = x + y 
y = x - y 
x = x - y 
print("x:",x,"y:",y)

# Using Built in Method you have swap it 
# Method is  

m = 10 
n = 20 
m , n = n ,m 
print("m:",m,"n:",n)

# OR 
def swap(p,q):
    return q,p

p = 10 
q = 20 
p , q = swap(p,q)
print("p:",p,"q:",q)

