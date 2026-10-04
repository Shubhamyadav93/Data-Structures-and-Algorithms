# a linked list node 
class Node:

    # constructor to initialize a new node with data
    def __init__(self,data):
        self.data = data
        self.next = None 

# function to traverse and print the singly linkedlist 
def traverseList(head):
    while head is not None:
        print(head.data,end="")
        if head.next is not None:
            print("->",end="")
        head = head.next 
    print()

if __name__ == "__main__":

    # create a hard-coded linked list 
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    traverseList(head)

# Here you can take take one function you can prit it all node means you can traversed all node then you print it 
# Here you can see you can create one function why? : --> Because you can print multiple time of node list insed of function you take here parameter you can take any parameter all notes are given in docs 
# Here you can take temp parameter 


# __________________________________________________________________________________________

class Node:
    # constructur you can initialize a new node with data 
    def __init__(self,data):
        self.data = data 
        self.next = None


# function you traversed and print singliy linkedlist 
def traversedlist(temp):
    while temp is not None:
        print(temp.data,end="->")
        temp = temp.next 
    print(None)



head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

traversedlist(head)



# __________________________________________________________________________________________


# Professional code  

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None # Shuruat ,me list khali hai 
    # Ab function ko hum main class ke ander likhenge  
    def traversalList(self):
        temp = self.head 
        while temp is not None: 
            print(temp.data,end="->")
            temp = temp.next 
        print("None")

# Main Program 
if __name__ == "__main__":
    # Pure management ab Linkedlist class karegi 
    my_list = Linkedlist()

    # Node banana or cunnect karna 
    my_list.head = Node(10)
    my_list.head.next = Node(20)
    my_list.head.next.next = Node(30)
    my_list.head.next.next.next = Node(40)

    my_list.traversalList()


# _________________-- OR-- _________________
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class Linkedlist:
    def __init__(self):
        self.head = None 
        
    def traveselist(self):
        temp = self.head 
        while temp is not None:
            print(temp.data , end="->")
            temp = temp.next 
        print("None")

my_list = Linkedlist()

my_list.node1 = Node(100)
my_list.node2 = Node(200)
my_list.node3 = Node(300)
my_list.node4 = Node(400)

my_list.head = my_list.node1

my_list.node1.next = my_list.node2
my_list.node2.next = my_list.node3 
my_list.node3.next = my_list.node4 

my_list.traveselist()

# _________________-- OR-- _________________


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkdlist:
    def __init__(self):
        self.head = None

    def traversedlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end="->")
            temp = temp.next
        print("None")

my_list = Linkdlist()
# 1. Nodes create karna
node1 = Node(1000)
node2 = Node(2000)
node3 = Node(3000)
node4 = Node(4000)

# # 2. SABSE IMPORTANT: 'head' set karna!
my_list.head = node1

# # 2. SABSE IMPORTANT: 'head' set karna!
node1.next = node2
node2.next = node3
node3.next = node4
# 4. Traversal function call karna
my_list.traversedlist()




## __________________________________________________________________________________________



                            #  GFG # 
# VS Code ke liye Complete Running Code

# Step 1: Pehle humne Node ka blueprint bana padega 
class Node:
    def __init__(self,x):
        self.data = x 
        self.next = None

# Step 2: GFG wali Solution Class jise tumne solve kiya tha 
class Solution:
    def printList(self,head):
        sol = []
        temp = head
        while temp is not None:
            sol.append(temp.data)
            temp = temp.next
        return sol 
    
# Step 3: Main Program (Jo GFG ka background manager banta hai)
if __name__ == "__main__":

    # ---- GFG BACKEND KA KAAM: LINKED LIST CREATION ---- 
    # Memory me manual nodes allocate our create karna [cite: 467,490]
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5) 

    # In sabhi nodes ko pointers ke through appas me connect karna [cite: 343]
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5 # node5.next automatic None rahega [cite : 343]

    #  ---- APNE FUNCTION KO CALL KARNA ----
    # Pehle Solution class ka ek instance (object) banayenge 
    obj = Solution()

    # Yaha humne fuction ko call kiya aur parameters me 'node1' (Head) ka address bhj diya [cite: 492]
    # GFG ka system bilkul isi tarah tumhare function ko 'head' data hai! [cite: 492]
    final_result = obj.printList(node1)

    # Terminal par result print karke check karna 
    print("Output Array:", final_result)



