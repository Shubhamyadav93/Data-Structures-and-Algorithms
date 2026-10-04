class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model

    def startEngine(self):
        print(f"{self.model} engin started")

    def stopEngine(self):
        print(f"{self.model} engine stopped")



myCar = Car("Red","Toyota")

print("My car color: ", myCar.color)
myCar.startEngine()
myCar.stopEngine()



# ____________________________________________________________________________________
# Example: Stack Using Class and Object

class Stack:

    def __init__(self):
        self.arr = [0]*5
        self.top = -1 

    # Method to push element
    def push(self,x):
        if(self.top == 4):
            print("Stack Overflow")
            return 
        
        self.top += 1
        self.arr[self.top] = x 

    # Method to pop element
    def pop(self):
        if(self.top == -1):
            print("SStaack Underflow")
            return 
        
        self.top -=1

    # Method to display stack 
    def display(self):
        for i in range(self.top,-1,-1):
            print(self.arr[i],end=" ")

        print()

if __name__ == "__main__":

    #  Creating stack object 
    s = Stack()

    # Performing operations
    s.push(10)
    s.push(20)
    s.push(30)

    print("Stack element: ", end=" ")
    s.display()

    s.pop()

    print("After pop: ", end="")
    s.display()

# Stack element:  30 20 10 
# After pop: 20 10 


