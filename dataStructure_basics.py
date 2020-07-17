# This is a python file for using implementing basic data structures using python
# =============================================================#
import sys
import datetime
"""
0. Linked List
1. Stack 
2. Queue 
3. Circular queue
4. Tree
5. Graph
"""
# =============================================================#
print("Hello World, this is Data Structure in python implementation")
print("Major version = ", sys.version_info.major,
      "\nMinor version = ", sys.version_info.minor)
print("Run Date & Time = ", datetime.datetime.now())

# =============================================================#


# =============================================================#

#=======================Array==================================#
# arrayName = array(typecode, [Initializers])


# By importing libray for Array in Python 
import array

# Defining array class 
"""
class array:
    def __init__(self):
        self.typecode = ''
        self.empty_list = []
    def array(self, typecode, arr):
        if 
"""

# i --> typecode for integers 
# b 	Represents signed integer of size 1 byte/td>
# B 	Represents unsigned integer of size 1 byte
# c 	Represents character of size 1 byte
# i 	Represents signed integer of size 2 bytes
# I 	Represents unsigned integer of size 2 bytes
# f 	Represents floating point of size 4 bytes
# d 	Represents floating point of size 8 bytes

arr = array.array('i', [100, 101, 103, 104, 100]) 

# Print all component of an array 
def print_array(arr):

    for i in arr:
        print(i, end=' ')

def learnArray():

    # Adding data to an Array
    arr.append(999)

    # Inserting data into an Array at specific position
    print (arr.insert(0,199))

    # Find index 
    print (arr.index(999))

    # Counting the of occurance of 100 in an array
    print (arr.count(100))

    # Remove data from Array 
    arr.remove(101)

    # Print data in an Array
    print_array(arr)


#=======================Linked List Class======================================#

# Linked List

#   A Linked List is a linear collection of data elements, called nodes, each pointing to the next node by means of a pointer. It is a data structure consisting of a group of nodes which together represent a sequence.
#   Singly-linked list: linked list in which each node points to the next node and the last node points to null
#   Doubly-linked list: linked list in which each node has two pointers, p and n, such that p points to the previous node and n points to the next node; the last node's n pointer points to null
#   Circular-linked list: linked list in which each node points to the next node and the last node points back to the first node
#   Time Complexity:
#       Access: O(n)
#       Search: O(n)
#       Insert: O(1)
#       Remove: O(1)

#   They can be used in various data structure like stack, queue and trees
#   https://www.youtube.com/watch?v=FSsriWQ0qYE
#   https://realpython.com/linked-lists-python/ "Reference"
#   https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm


class Node(object):
    'Node initiation'
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = None
        self.count = 0
    
    def size (self):
        return self.count
        
       
    def add_beg(self, data):
        new_node = Node(data)
        head_node = self.head
        new_node.next = head_node
        self.head = new_node
        self.count += 1
    
    def add_middle(self, data, position):
        new_node = Node(data)
        current_node = self.head
        if current_node == None:
            print ("Empty Node")
            return False

        for i in range(0, position-1):
            current_node = current_node.next
        temp_node = current_node.next    
        current_node.next = new_node
        new_node.next = temp_node
        self.count += 1
        
        
    def add_node(self,data):
        'The trick is loop till the end and add the node'
        new_node = Node(data)
        current_node = self.head
        if current_node == None:
            self.head = new_node
            self.count +=1
            return True
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        self.count +=1

    def delete_first(self):
        current_node = self.head
        self.head = current_node.next
        self.count -= 1
        return True 
        
    def delele_mid(self,position):
        current_node = self.head
        previous_node = self.head
        
        for _ in range(0, position-1):
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = current_node
        self.count -= 1
        return True 

    def delete_last(self):
        current_node = self.head
        previous_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        self.count -= 1
        return True 

    def print_node(self):
        current = self.head
        if current == None:
            print("No node associated with the head")
        while current:
            print (current.data, end='->')
            current = current.next
        print("None")
            
#=============================================================================#           
#=======================Linked List test======================================#


def learnLinkedList():
    print("\nInitializing Linked List\n")
    ll = LinkedList()

    print ("\nGetting Size of the Linked list\n")
    print(ll.size())

    print ("\nAdding node on the 3rd position")
    ll.add_middle(3.4,3)

    print ("\nAdding node at the end of the Linked List\n")
    ll.add_node(1)

    print ("\nAdding node at the end of the Linked List\n")
    ll.add_node(2)

    print ("\nAdding node at the end of the Linked List\n")
    ll.add_node(3)

    print ("\nAdding node at the end of the Linked List\n")
    ll.add_node(4)

    print ("\nAdding node at the begining of the Linked List\n")
    ll.add_beg(0)

    print("\nPrint all nodes")
    ll.print_node()

    print ("\nAdding node on the 3rd position")
    ll.add_middle(2.5,3)

    print("\nPrint all nodes\n")
    ll.print_node()

    print("Deleting first node")
    ll.delete_first()

    print("\nPrinting all nodes")
    ll.print_node()

    print("\nDeleting Last node")
    ll.delete_last()

    print("\nDeleting Mid node")
    ll.delele_mid(2)

    print("\nPrinting all nodes")
    ll.print_node()

    print ("\nGetting Size of the Linked list")
    print(ll.size())

#=============================================================================#
#======================== Doubbly linked list ================================#
# In Doubbly linked list every link has access its previous and next link
# https://www.tutorialspoint.com/python_data_structure/python_advanced_linked_list.htm

class DoublyNode:
    def __init__(self, data=None):
        'Initializing DoublyLinked Node list'
        self.left = None
        self.data = data 
        self.right = None
        
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.count = 0
        
    def size(self):
        return self.count

    def delete_first(self):
        if self.head == None:
            print("Empty list")
        else :
            self.head = self.head.right
            self.count -= 1
            return True

    def delete_mid(self, position):
        current_node = self.head 
        if current_node == None:
            print("Empty list")
        else :
            for _ in range(0, position-1):
                previous_node = current_node
                current_node = current_node.right
        
            temp_node = previous_node
            previous_node.right = current_node.right
            temp_node.left = previous_node 
            self.count -= 1

    def delete_last(self):
        current_node = self.head
        if current_node == None:
            print("Empty List")
            return False
        else :
            while current_node:
                previous_node = current_node.left
                current_node = current_node.right
            
            previous_node.right = None
            self.count -= 1

    def add_node(self, data):
        new_node = DoublyNode(data)
        current_node = self.head
        if current_node  == None:
            self.head = new_node
            new_node.left = self.head
            self.count += 1
            return True
        else :
            while current_node.right:
                current_node = current_node.right
            current_node.right = new_node
            new_node.left = current_node
            self.count += 1
            return True
    
    def print_list(self):
        current_node = self.head
        if current_node  == None:
            print("Empty Linked List")
        else :
            while current_node:
                print(current_node.data, end='->')
                current_node = current_node.right
            print("None")

#=============================================================================#
#====================== Doubly Linked List Test ===============================#
def learnDoublyLinkedList():
    print('\nInitiate Doubly linked list\n')

    dl = DoublyLinkedList()
    print("Adding node\n")
    dl.add_node(0)
    print("Adding node\n")
    dl.add_node(1)
    print("Adding node\n")
    dl.add_node(2)
    print("Adding node\n")
    dl.add_node(3)
    print("Adding node\n")
    dl.add_node(4)
    print("Adding node\n")
    dl.add_node(5)
    print("Adding node\n")
    print("\nPrinting all the nodes\n")
    dl.print_list()
    print(f"\nNumber of linked nodes = {dl.size()}\n")
    print("\nDeleting first node\n")
    dl.delete_first()
    dl.print_list()
    print(f"\nNumber of linked nodes = {dl.size()}\n")
    print("\n Deleting third node \n")
    dl.delete_mid(3)
    dl.print_list()
    print(f"\nNumber of linked nodes = {dl.size()}\n")
    print("\nDeleting Last Node\n")
    dl.delete_last()
    dl.print_list()
    print(f"\nNumber of linked nodes = {dl.size()}\n")

#=============================================================================#
#====================== Stack using Lists ====================================#
# Reference  https://www.tutorialspoint.com/python_data_structure/python_stack.htm

# Program to create a stack data structure in Python using list
a = []  # create a default list of all zeros
top = 0
print("\nProgram to create a stack data structure in Python using list \n")


def Push(n):                    # Push function: Push data on the stack
    global top                  # specify the 'top' variable is global
    a.append(n)
    #a[top] = n     # store the value at the top of stack
    top = top + 1               # increment the top
    #print("Top = ", top)       # print the top position number after each Push operation


def PrintStack():
    index = 0
    global top
    while index < top:
        print(a[index], "|", end=" "),
        index = index + 1
    print()

def Peek(): # Fetch the last vaule of the stack
    print (a[-1])

def Pop():  # Pop function: remove data from top of stack
    global top  # specify the 'top' variable is global
    top = top - 1  # decrement the top variable
    print("Top = ", top)  # print the top position number after each Push operation


def learnStack():
    print(a)
    Push(5)  # Push and Pop operation
    Push(6)
    Push(27)
    Push(90)
    Push(50)
    Push(38)
    Pop()
    Peek()
    Pop()
    print(a)  # Print the updated list after all operations




#==============================================================================#
#========================= Queue ==============================================#

# Queue supports first come first serve 
class Queue:
    def __init__(self):
        self.queue = list()

    def __sizeof__(self):
        return len(self.queue)
    
    def add_queue(self, data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        else:
            return False

    def remove_queue(self):
        if len(self.queue) <= 0:
            print("Empty Queue")
        else:
            self.queue.pop()

    def print_queue(self):
        for data in self.queue:
            print (data, end="->")
        
# =============================================================================#
# ======================== Queue Test =========================================#
    
def learnQueue():
    que = Queue()

    print("\nAdding data into the queue")
    que.add_queue(0)
    que.add_queue(1)
    que.add_queue(2)
    que.add_queue(3)
    que.add_queue(4)

    print("\nPrinting Queue")
    que.print_queue()

    print("\nRemove from Queue")
    que.remove_queue()

    print("\nPrinting Queue")
    que.print_queue()





#==============================================================================#
#========================= Dequeue ============================================#
# Dequeue is a Data stucture that combines features of Stack and Queue. In which 
# you can add data on both the end.

from collections import deque

# Initialization of Dequeue 
def learnDequeue():
    de = deque()

    print("\nAppending data into the dequeue")
    de.append(1)

    print("\nAppending data into the dequeue")
    de.append(2)

    print("\nAppending data into the left of dequeue")
    de.appendleft(0)

    print (de)
    print("\nPoping data from right\n")
    de.pop()

    print (de)
    print("\nPoping data from right\n")
    de.popleft()

    print (de)




# =============================================================================#
# ======================== Run test ===========================================#


#learnLinkedList()
learnDoublyLinkedList()
#learnStack()
#learnArray()
#learnQueue()
#learnDequeue()



