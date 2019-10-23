"""
Now that you have an understanding of what nodes are, let’s see one way they can be implemented using Python.

We will use a basic node that contains data and one link to another node. The node’s data will be specified when creating the node and immutable (can’t be updated). The link will be optional at initialization and can be updated.

Remember that at the end of a node path, the link to the next node is null because there are no more nodes left. In Python, this means it will be set to None.

1. Begin by creating a new class, Node. Add an __init__ method in the Node class that takes a value and an optional link_node (default should be None). These should be saved to the corresponding self properties (self.value and self.link_node).


We need methods to access the data and link within the node. For this, we will use two getters, get_value and get_link_node.

These should each return their corresponding value on the self object.

2. Implement the get_value getter in the Node class.

3.Implement the get_link_node getter in the Node class.


We are only allowing the value of the node to be set upon creation. However, we want to allow updating the link of the node. For this, we will use a setter to modify the self.link_node attribute.

The method should be called set_link_node and should take link_node as an argument. It should then update the self.link_node attribute as appropriate.

4. Implement the set_link_node setter in the Node class.
"""

class Node:

  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

  # Define your get_value and get_link_node methods below:
  def get_value(self):
    return self.value

  def get_link_node(self):
    return self.link_node

  # Define your set_link_node method below:
  def set_link_node(self, link_node):
    self.link_node = link_node
