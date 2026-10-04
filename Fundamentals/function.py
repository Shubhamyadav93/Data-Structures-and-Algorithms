def fun():
    print("called fun")


print("Before calling fun")
fun()
fun()
print("After calling a fun")

# ___________________________________________________________________________

def printDate(d,m,y):
    return d + "-" + m + "-" + y 


print("India become Independent on")
ans = printDate("15","08","1947")
print(ans)

# ___________________________________________________________________________

def greet_msg():
    print("Hi")
    print("Welcome to GreeksforGreeks")

def exist_msg():
    print("Please vist again")
    print("Bye")

greet_msg()
print("Hope you are enjoying")
exist_msg() 
