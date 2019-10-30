from node import Node

class Stack:
    def __init__(self, name):
        self.size = 0
        self.top_item = None
        self.limit = 1000
        self.name = name

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("No more room")

    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        print('This stack is empty')

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()
