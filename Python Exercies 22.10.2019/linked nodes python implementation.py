"""
Node Implementation
Let’s implement a linked list in Python. As you might recall, each linked list is a sequential chain of nodes. So before we start building out the LinkedList itself, we want to build up a Node class in Python that we can use to build our data containers.

Remember that a node contains two elements:
- data
- a link to the next node

1. Within script.py in the pane to the right, create an empty Node class.

Inside, define an .__init__() method for the Node. It should take a value and a next_node.

next_node should default to None if not provided. These variables should be saved to self with corresponding key names.


2. Define .get_value() and .get_next_node() methods. These should return the corresponding values from self.

3. Define a .set_next_node() method that takes self and next_node as parameters and allows you to update the link to the next node.

4. Outside the Node class, create an instance of Node called my_node with a value of 44.
Use .get_value() to print the value of my_node.
"""

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

my_node = Node(44)
# print(my_node.get_value())

"""
With the Node in hand, we can start building the actual linked list. Depending on the end-use of the linked list, a variety of methods can be defined.

For our use, we want to be able to:

- get the head node of the list (it’s like peeking at the first item in line)
- add a new node to the beginning of the list
- print out the list values in order
- remove a node that has a particular value

1. Within script.py in the pane to the right, create an empty LinkedList class.

Define an .__init__() method for the LinkedList. We want to be able to instantiate a LinkedList with a head node, so .__init__() should take value as an argument. Make sure value defaults to None if no value is provided.

Inside the .__init__() method, set self.head_node equal to a new Node with value as its value.

2 .Define a .get_head_node() method that helps us peek at the first node in the list.

Inside the method, return the head node of the linked list.
"""

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node
