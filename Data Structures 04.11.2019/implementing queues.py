class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

  def get_next_node(self):
    return self.next_node

  def get_value(self):
    return self.value


class Queue:
  # Add max_size and size properties within __init__():
  def __init__(self, max_size=None):
    self.max_size = max_size
    self.head = None
    self.tail = None
    self.size = 0

  def peek(self):
    if self.get_size() == 0:
      print("Nothing to see here!")
    else:
      return self.head.get_value()

  # Define get_size() and has_space() below:
  def get_size(self):
    return self.size

  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()

  def is_empty(self):
    if self.size == 0:
      return True
    else:
      return False
