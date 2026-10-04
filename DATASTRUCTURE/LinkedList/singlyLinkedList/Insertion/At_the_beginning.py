# Define a node in the Linked list
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

# Function to inserta new node 
# at the beginning of the list 
def insertAtFront(head,x):
    newNode = Node(x)
    newNode.next = head
    return newNode 

# Function to print thecontents 
# of the linked list 
def printList(head):
    temp = head
    while temp is not None:
        print(temp.data,end="->")
        temp = temp.next 
    print("None")


if __name__ == "__main__":
    # Create the linked list 2->3->4->5
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    # Insert a new node at 
    # the front of the list 
    x = 1 
    head = insertAtFront(head,x)

    # print the update list 
    printList(head) 


