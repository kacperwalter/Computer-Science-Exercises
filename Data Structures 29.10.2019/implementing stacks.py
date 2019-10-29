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

3. In __init__(), let’s add two new properties: size and limit.

limit should be accepted as a parameter with a default of 1000. Inside the method, set the instance limit property to the passed in value of limit.

size should be set to 0 in __init__().

4. In peek() and pop(), wrap the current body of each method in an if clause that checks if the size of the stack is greater than 0.

At the end of each method, outside the if clause, add an else clause with a print statement to let users know that the stack is empty.

5. In pop() just before the return statement, reduce the size of the stack by 1.
"""

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.limit = limit
    self.size = 0

  def push(self, value):
    item = Node(value)
    item.set_next_node(self.top_item)
    self.top_item = item

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      # Decrement the stack size here:
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    else:
      print("Nothing to see here!")
