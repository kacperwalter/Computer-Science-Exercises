class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

  def get_value(self):
    return self.value

  def get_link_node(self):
    return self.link_node

  def set_link_node(self, link_node):
    self.link_node = link_node

""""
1. Below __init__(), define a method push() for Stack that takes the parameter value. Inside the method:

Instantiate a Node with value as an argument and assign it to the variable item (because this item is a node, we have easy access to Node’s class methods)
Set item‘s next node to the stack’s current top_item using the Node method set_next_node()
Set the stack instance’s top_item equal to the new item, adding it to the top of the stack

2. Below push(), define a method pop() for Stack. Inside pop():

Create a variable item_to_remove and set it equal to the stack’s top_item
If we’re removing our stack’s top_item, we need to set a new top_item! Set the top_item equal to the node after item_to_remove
Return the value stored in item_to_remove
"""

class Stack:
  def __init__(self):
    self.top_item = None

  def peek(self):
    return self.top_item.get_value()

  def push(self, value):
    item = Node(value)
    item.set_next_node(self.top_item)
    self.top_item = item

  def pop(self):
    item_to_remove = self.top_item
    self.top_item = item_to_remove
    return item_to_remove.value

  def peek(self):
    return self.top_item.get_value()
