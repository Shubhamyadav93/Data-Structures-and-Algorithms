# constructure to inialize a new node with data 
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

# Create the first node (head of the list)
head = Node(10)
# Link the secound Node 
head.next = Node(20)

# Link the third node 
head.next.next = Node(30)

# Link the fourth node 

head.next.next.next = Node(40)

# Printing the linkedlist 
temp = head 
while temp is not None:
    print(temp.data,end=" ")
    temp = temp.next 





