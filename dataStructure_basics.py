# This is a python file for using implementing basic data structures using python
# =============================================================#
import sys
import datetime

# =============================================================#
print("Hello World, this is python learning codebase")
print("Major version = ", sys.version_info.major,
      "\nMinor version = ", sys.version_info.minor)
print("Run Date & Time = ", datetime.datetime.now())

# =============================================================#

# Program to create a stack data structure in Python using list
a = [0, 0, 0, 0, 0]  # create a default list of all zeros
top = 0
print("Program to create a stack data structure in Python using list \n")

def Push(n):  # Push function: Push data on the stack
    global top  # specify the 'top' variable is global
    a[top] = n  # store the value at the top of stack
    top = top + 1  # increment the top
    print
    top  # print the top position number after each Push operation


def Pop():  # Pop function: remove data from top of stack
    global top  # specify the 'top' variable is global
    top = top - 1  # decrement the top variable
    print
    top  # print the top position number in array


Push(5)  # Push and Pop operation
Push(6)
Push(27)
Pop()
Pop()

print(a)  # Print the updated list after all operations
# =============================================================#

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

        for i in range(0, position):
            current_node = current_node.next
        temp_node = current_node.next    
        current_node.next = new_node
        new_node.next = temp_node
        self.count += 1
        
        
    def add_node(self,data):
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

    def print_node(self):
        current = self.head
        if current == None:
            print("No node associated with the head")
        while current != None:
            print (current.data, end='->')
            current = current.next
        print("None")
            
#=============================================================================#           
#=======================Linked List test======================================#
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
ll.add_middle(3.4,3)

print("\nPrint all nodes\n")
ll.print_node()
print ("\nGetting Size of the Linked list")
print(ll.size())
        

        





    





